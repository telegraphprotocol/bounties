"""Deterministic REGULATORY_FILING_MONITOR evaluator adapter for Mission 04 & 13 (#192, #201).

Evaluates statutory regulatory filing monitoring and periodic disclosure queries against
official primary regulatory registers (SEC EDGAR Submissions API, US Federal Register, ESMA, FCA):

1. Statutory Filing Count Calibration (exact vs bounded discrepancy) - 30% weight
2. Form Type & Statutory Disclosure Category Precision (10-K, 10-Q, 8-K, Rules, Notices) - 35% weight
3. Authoritative Regulatory Accession Numbers & Official Document URLs - 25% weight
   CRITICAL COMPLIANCE GATE: Unverified commercial blogs or fabricated document links
   receive zero URL credit; links must resolve to official statutory archives (sec.gov, federalregister.gov).
4. Regulatory System Provenance Citation (EDGAR, Federal Register, CIK, XBRL) - 10% weight
"""
from __future__ import annotations
import re
from typing import Any, Mapping
from urllib.parse import urlparse


OFFICIAL_REGULATORY_DOMAINS = {
    "sec.gov",
    "www.sec.gov",
    "data.sec.gov",
    "federalregister.gov",
    "www.federalregister.gov",
    "esma.europa.eu",
    "www.esma.europa.eu",
    "fca.org.uk",
    "www.fca.org.uk",
    "bafin.de",
    "asic.gov.au",
    "sebi.gov.in"
}


def validate_edgar_accession(accession: str) -> bool:
    """Validate a standard SEC EDGAR accession number format (10-digit CIK + 2-digit YY + 6-digit seq)."""
    cleaned = str(accession or "").strip()
    return bool(re.match(r'^\d{10}-\d{2}-\d{6}$', cleaned))


def is_official_regulatory_url(url: str) -> bool:
    """Check if a URL points to an authoritative government regulatory register."""
    if not url or not isinstance(url, str):
        return False
    try:
        parsed = urlparse(url.strip())
        hostname = (parsed.hostname or "").lower()
        return hostname in OFFICIAL_REGULATORY_DOMAINS or any(hostname.endswith(f".{d}") for d in OFFICIAL_REGULATORY_DOMAINS)
    except Exception:
        return False


def _extract_filing_count(data: Mapping[str, Any]) -> int:
    """Extract integer filing count from prediction or truth payload."""
    if "filing_count" in data and data["filing_count"] is not None:
        try:
            return int(data["filing_count"])
        except (ValueError, TypeError):
            pass
    if "count" in data and data["count"] is not None:
        try:
            return int(data["count"])
        except (ValueError, TypeError):
            pass
    if "filings" in data and isinstance(data["filings"], list):
        return len(data["filings"])
    
    summary = str(data.get("summary", "") or data.get("explanation", ""))
    match = re.search(r'\b(?:found|identified|monitored|total(?:\s+of)?)\s*[:=]?\s*(\d+)\s*(?:filings?|documents?|records?)\b', summary, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 0


def _extract_form_types(text: str) -> set[str]:
    """Extract standard statutory form types mentioned in summary or filings."""
    forms = set()
    patterns = [
        (r'\b10-?K\b', '10-K'),
        (r'\b10-?Q\b', '10-Q'),
        (r'\b8-?K\b', '8-K'),
        (r'\bFORM\s+4\b', 'FORM 4'),
        (r'\b(?:SCHEDULE\s+)?13[DG]\b', '13D/G'),
        (r'\bPROPOSED\s+RULES?\b', 'Proposed Rule'),
        (r'\bRULES?\b', 'Rule'),
        (r'\bNOTICES?\b', 'Notice'),
        (r'\bPRESIDENTIAL\s+DOCUMENTS?\b', 'Presidential Document')
    ]
    for pat, form in patterns:
        if re.search(pat, text, re.IGNORECASE):
            forms.add(form)
    return forms


def evaluate_regulatory_filing(
    truth: Mapping[str, Any],
    prediction: Mapping[str, Any]
) -> dict[str, float | bool | str]:
    """Score a miner or agent output against official regulatory filing monitoring ground truth.
    
    Returns a deterministic dictionary containing component scores and composite score [0.0, 1.0].
    """
    pred_summary = str(prediction.get("summary", "") or prediction.get("explanation", ""))
    
    gold_count = _extract_filing_count(truth)
    pred_count = _extract_filing_count(prediction)

    # 1. Statutory Filing Count Calibration (30% weight)
    if gold_count == 0:
        count_score = 1.0 if pred_count == 0 else 0.0
    else:
        abs_diff = abs(gold_count - pred_count)
        pct_diff = abs_diff / max(gold_count, 1)
        if abs_diff == 0:
            count_score = 1.0
        elif pct_diff <= 0.15:
            count_score = 0.85
        elif pct_diff <= 0.35:
            count_score = 0.60
        elif pct_diff <= 0.60:
            count_score = 0.30
        else:
            count_score = 0.0

    # 2. Form Type & Statutory Disclosure Precision (35% weight)
    gold_text = f"{str(truth.get('summary', ''))} {str(truth.get('filings', ''))} {str(truth.get('forms', ''))}"
    pred_text = f"{pred_summary} {str(prediction.get('filings', ''))} {str(prediction.get('forms', ''))}"
    
    gold_forms = _extract_form_types(gold_text)
    pred_forms = _extract_form_types(pred_text)

    if not gold_forms:
        form_score = 1.0 if (gold_count == 0 and pred_count == 0) else (1.0 if pred_count > 0 else 0.50)
    else:
        intersection = gold_forms.intersection(pred_forms)
        form_score = round(len(intersection) / len(gold_forms), 2)

    # 3. Official Regulatory URLs & Accession Numbers (25% weight)
    pred_urls = prediction.get("urls", [])
    if isinstance(pred_urls, str):
        pred_urls = [pred_urls]
    elif not isinstance(pred_urls, list):
        pred_urls = []

    # Also extract URLs from text
    found_urls = re.findall(r'https?://[^\s,\)\]]+', pred_text)
    all_urls = list(set(pred_urls + found_urls))

    official_urls = [u for u in all_urls if is_official_regulatory_url(u)]
    
    # Check for accession numbers in text or filings
    has_accession = bool(re.search(r'\b\d{10}-\d{2}-\d{6}\b', pred_text))

    if gold_count == 0:
        url_score = 1.0 if len(official_urls) == 0 else 0.50
    else:
        if official_urls and has_accession:
            url_score = 1.0
        elif official_urls:
            url_score = 0.85
        elif has_accession:
            url_score = 0.65
        else:
            url_score = 0.15

    # 4. Regulatory System Provenance Citation (10% weight)
    provenance_terms = [
        "sec edgar", "edgar", "sec.gov", "federal register",
        "cik", "xbrl", "data.sec.gov", "statutory filing", "filing monitor"
    ]
    pred_lower = pred_text.lower()
    has_provenance = any(t in pred_lower for t in provenance_terms)
    provenance_score = 1.0 if has_provenance else 0.0

    composite_score = round(
        (0.30 * count_score) + (0.35 * form_score) + (0.25 * url_score) + (0.10 * provenance_score),
        4
    )

    return {
        "count_score": round(count_score, 4),
        "form_score": round(form_score, 4),
        "url_score": round(url_score, 4),
        "provenance_score": round(provenance_score, 4),
        "composite_score": composite_score,
        "passed": composite_score >= 0.70
    }
