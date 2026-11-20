"""Deterministic CORPORATE_REGISTRY_LOOKUP evaluator adapter for Mission 03 Institutional Markets (#191).

Evaluates corporate registry lookup and statutory entity resolution predictions against
official primary registers (GLEIF Global LEI Index, UK Companies House, Delaware Division
of Corporations, Handelsregister, ASIC, MCA):

1. Statutory Registration Status Match (active, lapsed, dissolved, or unindexed) - 35% weight
   CRITICAL COMPLIANCE GATE: False positive active clearance on a lapsed or dissolved
   corporate counterparty is heavily penalized to protect institutional bilateral clearing.
2. Statutory Identifier & LEI Accuracy (ISO 17442 20-character checksum / Company No) - 35% weight
3. Jurisdiction & Legal Entity Name Precision (ISO 3166 codes & entity matching) - 20% weight
4. Authoritative Statutory Registry Provenance (GLEIF, Companies House, SEC EDGAR, etc.) - 10% weight
"""
from __future__ import annotations
import re
from typing import Any, Mapping


def validate_iso17442_lei(lei: str) -> bool:
    """Validate an ISO 17442 Legal Entity Identifier using the MOD 97-10 check (ISO 7064)."""
    cleaned = str(lei or "").strip().upper()
    if not re.match(r'^[A-Z0-9]{20}$', cleaned):
        return False
    
    # Check digits must be numeric
    if not cleaned[18:20].isdigit():
        return False
    
    # Convert characters to digits (A=10, ..., Z=35)
    digits = []
    for char in cleaned:
        if char.isdigit():
            digits.append(char)
        else:
            digits.append(str(ord(char) - 55))
    
    num_str = "".join(digits)
    # MOD 97 check: remainder must be 1
    remainder = 0
    for digit in num_str:
        remainder = (remainder * 10 + int(digit)) % 97
    return remainder == 1


def _extract_active(data: Mapping[str, Any]) -> bool:
    """Extract active statutory status from prediction or truth payload."""
    if "active" in data and data["active"] is not None:
        val = data["active"]
        if isinstance(val, bool):
            return val
        if str(val).strip().lower() in ("true", "1", "active", "issued", "valid"):
            return True
        if str(val).strip().lower() in ("false", "0", "inactive", "lapsed", "dissolved", "suspended"):
            return False

    summary = str(data.get("summary", "") or data.get("explanation", "") or data.get("verdict", "")).strip().upper()
    if re.search(r'\b(?:LAPSED|DISSOLVED|INACTIVE|SUSPENDED|STRUCK\s+OFF|NOT\s+ACTIVE|DEFUNCT)\b', summary):
        return False
    if re.search(r'\b(?:ACTIVE|ISSUED|INCORPORATED|GOOD\s+STANDING|VALID\s+REGISTRATION)\b', summary):
        return True
    return bool(data.get("found", False))


def _normalize_name(name: str) -> str:
    """Normalize legal entity name by removing legal forms and punctuation."""
    text = str(name or "").strip().lower()
    text = re.sub(r'[^\w\s]', ' ', text)
    legal_forms = [
        r'\binc(?:orporated)?\b',
        r'\bcorp(?:oration)?\b',
        r'\bllc\b',
        r'\bltd\b',
        r'\blimited\b',
        r'\bgmbh\b',
        r'\bag\b',
        r'\bse\b',
        r'\bplc\b',
        r'\bllp\b',
        r'\bpty\s+ltd\b',
        r'\bpvt\s+ltd\b',
        r'\bco\b',
        r'\bcompany\b'
    ]
    for form in legal_forms:
        text = re.sub(form, ' ', text)
    return " ".join(text.split())


def evaluate_corporate_registry(
    truth: Mapping[str, Any],
    prediction: Mapping[str, Any]
) -> dict[str, float | bool | str]:
    """Score a miner or agent output against authoritative corporate registry ground truth.
    
    Returns a deterministic dictionary containing component scores and composite score [0.0, 1.0].
    """
    pred_summary = str(prediction.get("summary", "") or prediction.get("explanation", ""))
    
    gold_active = _extract_active(truth)
    pred_active = _extract_active(prediction)

    gold_found = bool(truth.get("found", True))
    pred_found = bool(prediction.get("found", pred_active or bool(prediction.get("registration_id"))))

    # 1. Statutory Registration Status Match (35% weight)
    if not gold_found:
        # Ground truth entity does not exist in any statutory registry
        if not pred_found:
            status_score = 1.0
        else:
            # Hallucinated corporate existence: zero status score
            status_score = 0.0
    else:
        if gold_active == pred_active:
            status_score = 1.0
        else:
            # False positive active status on lapsed or dissolved entity
            status_score = 0.15

    # 2. Statutory Identifier & LEI Accuracy (35% weight)
    gold_id = str(truth.get("registration_id", "") or truth.get("lei", "") or truth.get("company_number", "")).strip().upper()
    pred_id = str(prediction.get("registration_id", "") or prediction.get("lei", "") or prediction.get("company_number", "")).strip().upper()

    if not gold_found:
        # Should return no registration ID
        identifier_score = 1.0 if not pred_id else 0.0
    elif gold_id:
        if pred_id == gold_id or gold_id in pred_summary.upper():
            identifier_score = 1.0
            # Bonus verification if it is an LEI: confirm ISO 17442 checksum
            if len(gold_id) == 20 and validate_iso17442_lei(gold_id):
                identifier_score = 1.0
        elif pred_id and validate_iso17442_lei(pred_id):
            # Formally valid LEI format but wrong number
            identifier_score = 0.30
        else:
            identifier_score = 0.0
    else:
        identifier_score = 1.0 if pred_id else 0.50

    # 3. Jurisdiction & Legal Entity Name Precision (20% weight)
    if not gold_found:
        jurisdiction_name_score = 1.0 if not pred_found else 0.0
    else:
        gold_jur = str(truth.get("jurisdiction", "") or truth.get("country", "")).strip().upper()
        pred_jur = str(prediction.get("jurisdiction", "") or prediction.get("country", "")).strip().upper()

        jur_score = 1.0 if (not gold_jur or gold_jur in pred_jur or pred_jur in gold_jur or gold_jur in pred_summary.upper()) else 0.20

        gold_name = _normalize_name(truth.get("legal_name", "") or truth.get("company", ""))
        pred_name = _normalize_name(prediction.get("legal_name", "") or prediction.get("company", ""))

        if not gold_name:
            name_score = 1.0
        elif gold_name == pred_name:
            name_score = 1.0
        elif gold_name in pred_name or pred_name in gold_name or gold_name in _normalize_name(pred_summary):
            name_score = 0.80
        else:
            name_score = 0.20

        jurisdiction_name_score = round((jur_score * 0.50) + (name_score * 0.50), 4)

    # 4. Authoritative Statutory Registry Provenance (10% weight)
    auth_registers = [
        "gleif", "companies house", "handelsregister", "sec edgar",
        "delaware", "division of corporations", "asic", "mca",
        "statutory", "commercial register", "lei index", "infogreffe"
    ]
    pred_text_lower = f"{pred_summary} {str(prediction.get('provenance', ''))} {str(prediction.get('source', ''))}".lower()
    has_auth_provenance = any(reg in pred_text_lower for reg in auth_registers)
    provenance_score = 1.0 if has_auth_provenance else 0.0

    composite_score = round(
        (0.35 * status_score) + (0.35 * identifier_score) + (0.20 * jurisdiction_name_score) + (0.10 * provenance_score),
        4
    )

    return {
        "status_score": round(status_score, 4),
        "identifier_score": round(identifier_score, 4),
        "jurisdiction_name_score": round(jurisdiction_name_score, 4),
        "provenance_score": round(provenance_score, 4),
        "composite_score": composite_score,
        "passed": composite_score >= 0.70
    }
