"""Deterministic GRID_POWER_PRICE evaluator adapter for Missions 11, 12 (#199, #200).

Evaluates wholesale locational marginal electricity pricing (LMP) predictions against
official Regional Transmission Organization (RTO) and Independent System Operator (ISO)
settlement ground truth (CAISO OASIS, ERCOT Settlement Points, NYISO, PJM, MISO):

1. LMP Settlement Price Calibration (absolute & percentage tolerance) - 40% weight
   CRITICAL COMPLIANCE GATE: Inverted price signs or pricing variance > 30% receive zero price credit.
2. Pricing Node / Settlement Zone Identification (NP15, SP15, Houston Hub, etc.) - 30% weight
3. Market Category & Temporal Alignment (DAM vs RTM & ISO-8601 interval) - 20% weight
4. Authoritative Grid Operator Provenance Citation (CAISO, ERCOT, NYISO, FERC) - 10% weight
"""
from __future__ import annotations
import math
import re
from typing import Any, Mapping


def _extract_lmp_price(data: Mapping[str, Any]) -> float | None:
    """Extract numeric LMP price in USD/MWh from prediction or truth payload."""
    for key in ("lmp_usd_per_mwh", "price_mwh", "lmp", "price", "settlement_price"):
        if key in data and data[key] is not None:
            try:
                val = float(data[key])
                if not math.isnan(val):
                    return val
            except (ValueError, TypeError):
                pass
    
    summary = str(data.get("summary", "") or data.get("explanation", ""))
    match = re.search(r'([+-]?)\s*\$?\s*([+-]?\d+(?:\.\d+)?)\s*(?:USD)?\s*/?\s*(?:MWh|mwh)\b', summary)
    if match:
        try:
            sign = -1.0 if ('-' in (match.group(1) + match.group(2))) else 1.0
            num = abs(float(match.group(2)))
            return sign * num
        except ValueError:
            pass
    return None


def _normalize_node(node_str: str) -> str:
    """Normalize grid node or pricing hub name."""
    text = str(node_str or "").strip().upper()
    text = re.sub(r'[\(\)\[\],\.-]', ' ', text)
    tokens = text.split()
    return " ".join(tokens)


def _extract_market(data: Mapping[str, Any]) -> str:
    """Extract and normalize market interval category (DAM vs RTM)."""
    raw = str(data.get("market", "")).strip().upper()
    if "DAM" in raw or "DAY-AHEAD" in raw or "DAY AHEAD" in raw:
        return "DAM"
    if "RTM" in raw or "REAL-TIME" in raw or "REAL TIME" in raw or "HASP" in raw:
        return "RTM"
    
    summary = str(data.get("summary", "") or data.get("explanation", "")).upper()
    if re.search(r'\b(?:DAY-AHEAD|DAY AHEAD|DAM)\b', summary):
        return "DAM"
    if re.search(r'\b(?:REAL-TIME|REAL TIME|RTM|HASP|FIVE-MINUTE)\b', summary):
        return "RTM"
    return "UNKNOWN"


def evaluate_grid_power_price(
    truth: Mapping[str, Any],
    prediction: Mapping[str, Any]
) -> dict[str, float | bool | str]:
    """Score a miner or agent output against authoritative ISO/RTO grid power settlement ground truth.
    
    Returns a deterministic dictionary containing component scores and composite score [0.0, 1.0].
    """
    pred_summary = str(prediction.get("summary", "") or prediction.get("explanation", ""))
    
    gold_price = _extract_lmp_price(truth)
    pred_price = _extract_lmp_price(prediction)

    # 1. LMP Settlement Price Calibration (40% weight)
    if gold_price is None or pred_price is None:
        price_score = 0.0
    else:
        # Sign check (electricity prices can be negative during curtailment, but sign must match)
        if (gold_price > 0 and pred_price < 0) or (gold_price < 0 and pred_price > 0):
            price_score = 0.0
        else:
            abs_err = abs(gold_price - pred_price)
            # Use relative error scaled by magnitude
            denom = max(abs(gold_price), 10.0)
            rel_err = abs_err / denom

            if abs_err <= 0.01:
                price_score = 1.0
            elif rel_err <= 0.02:
                price_score = 0.95
            elif rel_err <= 0.05:
                price_score = 0.85
            elif rel_err <= 0.15:
                price_score = 0.50
            elif rel_err <= 0.30:
                price_score = 0.20
            else:
                price_score = 0.0

    # 2. Pricing Node / Settlement Zone Identification (30% weight)
    gold_node = _normalize_node(truth.get("node_or_zone", "") or truth.get("hub", ""))
    pred_node = _normalize_node(prediction.get("node_or_zone", "") or prediction.get("hub", ""))

    pred_full_text = f"{pred_node} {_normalize_node(pred_summary)}"
    if not gold_node:
        node_score = 1.0 if pred_node else 0.50
    elif gold_node in pred_full_text or pred_node in gold_node:
        node_score = 1.0
    else:
        # Partial token match (e.g. NP15 in CAISO NP15)
        gold_tokens = set(gold_node.split())
        pred_tokens = set(pred_full_text.split())
        if gold_tokens and gold_tokens.intersection(pred_tokens):
            node_score = 0.75
        else:
            node_score = 0.0

    # 3. Market Category & Temporal Alignment (20% weight)
    gold_market = _extract_market(truth)
    pred_market = _extract_market(prediction)
    market_match = (gold_market == pred_market) if gold_market != "UNKNOWN" else True

    gold_interval = str(truth.get("interval_start", "")).strip()
    pred_interval = str(prediction.get("interval_start", "")).strip()
    interval_match = (gold_interval in pred_interval or pred_interval in gold_interval or gold_interval in pred_summary) if gold_interval else True

    market_temporal_score = round(
        (0.60 * (1.0 if market_match else 0.20)) +
        (0.40 * (1.0 if interval_match else 0.30)),
        4
    )

    # 4. Authoritative Grid Operator Provenance Citation (10% weight)
    operator_terms = [
        "caiso", "ercot", "nyiso", "pjm", "miso", "spp",
        "iso-ne", "oasis", "settlement point", "ferc", "lmp"
    ]
    pred_lower = f"{pred_summary} {str(prediction.get('provenance', ''))} {str(prediction.get('iso', ''))}".lower()
    has_operator_provenance = any(op in pred_lower for op in operator_terms)
    provenance_score = 1.0 if has_operator_provenance else 0.0

    composite_score = round(
        (0.40 * price_score) + (0.30 * node_score) + (0.20 * market_temporal_score) + (0.10 * provenance_score),
        4
    )

    return {
        "price_score": round(price_score, 4),
        "node_score": round(node_score, 4),
        "market_temporal_score": round(market_temporal_score, 4),
        "provenance_score": round(provenance_score, 4),
        "composite_score": composite_score,
        "passed": composite_score >= 0.70
    }
