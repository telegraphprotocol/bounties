"""Deterministic SANCTIONS_SCREENING_MATCH evaluator adapter for Mission 02 Stablecoin (#190).

Evaluates sanctions screening predictions against official US Treasury OFAC SDN ground truth:
1. Verdict classification accuracy (SANCTIONS MATCH vs NO SANCTIONS MATCH) - 40% weight
   CRITICAL COMPLIANCE GATE: False negatives (clearing a designated entity/address) immediately score 0.0.
2. SDN Identifier & Program Recall (UID, Sanctions Program, or EVM digital currency address) - 30% weight
3. Matching confidence & similarity calibration (exact vs fuzzy bigram thresholds) - 20% weight
4. Authoritative compliance provenance citation (OFAC, SDN, 31 CFR, FinCEN) - 10% weight
"""
from __future__ import annotations
import re
from typing import Any, Mapping


def _is_match(data: Mapping[str, Any]) -> bool:
    if "matched" in data:
        return bool(data["matched"])
    verdict = str(data.get("verdict", "")).strip().upper()
    summary = str(data.get("summary", "") or data.get("explanation", "")).strip().upper()
    text = f"{verdict} {summary}"

    if re.search(r'\b(?:NO\s+SANCTIONS\s+MATCH|CLEAN\s+COUNTERPARTY|NOT\s+SANCTIONED|NOT\s+MATCHED|MATCH_FOUND:\s*FALSE)\b', text):
        return False
    if re.search(r'\b(?:SANCTIONS\s+MATCH|BLOCKED\s+COUNTERPARTY|PROHIBITED\s+COUNTERPARTY|SDN\s+MATCH|MATCH_FOUND:\s*TRUE)\b', text):
        return True
    return False


def evaluate_sanctions_screening(
    truth: Mapping[str, Any],
    prediction: Mapping[str, Any]
) -> dict[str, float | bool | str]:
    """Score a miner or agent output against OFAC sanctions screening ground truth.
    
    Returns a deterministic dictionary containing component scores and composite score [0.0, 1.0].
    """
    pred_summary = str(prediction.get("summary", "") or prediction.get("explanation", ""))
    
    gold_is_match = _is_match(truth)
    pred_is_match = _is_match(prediction)

    # ZERO-TOLERANCE COMPLIANCE FAIL-CLOSED GATE:
    # If gold is a sanctions match, but prediction cleared it -> instant 0.0 composite score.
    if gold_is_match and not pred_is_match:
        return {
            "verdict_score": 0.0,
            "identifier_score": 0.0,
            "similarity_score": 0.0,
            "provenance_score": 0.0,
            "composite_score": 0.0,
            "passed": False,
            "breach": "CRITICAL_FALSE_NEGATIVE: Sanctioned entity or address was erroneously cleared."
        }

    # 1. Verdict Match (40% weight)
    if gold_is_match == pred_is_match:
        verdict_score = 1.0
    else:
        # False positive (flagged clean vendor): penalized to 0.20
        verdict_score = 0.20

    # 2. Identifier & Program Recall (30% weight)
    gold_uid = str(truth.get("uid", "")).strip()
    gold_program = str(truth.get("program", "")).strip().upper()
    gold_address = str(truth.get("address", "")).strip().lower()

    if gold_is_match:
        id_checks = 0
        id_matches = 0

        if gold_uid:
            id_checks += 1
            if gold_uid in pred_summary or str(prediction.get("uid", "")) == gold_uid:
                id_matches += 1

        if gold_program:
            id_checks += 1
            if gold_program in pred_summary.upper() or str(prediction.get("program", "")).upper() == gold_program:
                id_matches += 1

        if gold_address:
            id_checks += 1
            if gold_address in pred_summary.lower() or str(prediction.get("address", "")).lower() == gold_address:
                id_matches += 1

        identifier_score = round(id_matches / id_checks, 2) if id_checks > 0 else 1.0
    else:
        # For clean queries, verify 0 matches were returned
        matches_count = prediction.get("matches_count", 0) or len(prediction.get("matches", []))
        identifier_score = 1.0 if (matches_count == 0 and not pred_is_match) else 0.0

    # 3. Matching Similarity Calibration (20% weight)
    gold_similarity = float(truth.get("similarity", 1.0 if gold_is_match else 0.0))
    pred_similarity = float(prediction.get("similarity", prediction.get("confidence", 1.0 if pred_is_match else 0.0)))
    
    sim_diff = abs(gold_similarity - pred_similarity)
    if sim_diff <= 0.15:
        similarity_score = 1.0
    elif sim_diff <= 0.35:
        similarity_score = 0.50
    else:
        similarity_score = 0.0

    # 4. Provenance Citation (10% weight)
    auth_citations = ["ofac", "sdn", "treasury", "31 cfr", "sanctions", "fincen"]
    has_auth_citation = any(c in pred_summary.lower() or c in str(prediction.get("provenance", "")).lower() for c in auth_citations)
    provenance_score = 1.0 if has_auth_citation else 0.0

    composite_score = round(
        (0.40 * verdict_score) + (0.30 * identifier_score) + (0.20 * similarity_score) + (0.10 * provenance_score),
        4
    )

    return {
        "verdict_score": round(verdict_score, 4),
        "identifier_score": round(identifier_score, 4),
        "similarity_score": round(similarity_score, 4),
        "provenance_score": round(provenance_score, 4),
        "composite_score": composite_score,
        "passed": composite_score >= 0.70
    }
