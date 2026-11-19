"""Deterministic CONTRACT_OBLIGATION_AUDIT evaluator adapter for Mission 04 Legal (#192).

Evaluates contract audit predictions against statutory ground truth:
1. Verdict accuracy (COMPLIANT, BREACH, DELAY_PENALTY, HOLD_NOTICE)
2. Statutory and clause citation recall (e.g., MahaRERA, FIDIC, MSMED Act)
3. Deterministic penalty arithmetic within basis-point tolerance
"""
from __future__ import annotations
import math
from typing import Any, Mapping, Sequence


def evaluate_contract_obligation(
    truth: Mapping[str, Any],
    prediction: Mapping[str, Any],
    penalty_tolerance_bps: int = 100
) -> dict[str, float | bool | str]:
    """Score a miner or agent output against contract obligation ground truth.
    
    Returns a deterministic dictionary containing component scores and composite score [0.0, 1.0].
    """
    # 1. Verdict Matching (40% weight)
    gold_verdict = str(truth.get("verdict", "")).strip().upper()
    pred_verdict = str(prediction.get("verdict", "")).strip().upper()
    verdict_score = 1.0 if gold_verdict == pred_verdict and gold_verdict else 0.0

    # 2. Citation Recall (30% weight)
    gold_citations = {str(c).strip().lower() for c in truth.get("citations", [])}
    pred_citations = {str(c).strip().lower() for c in prediction.get("citations", [])}
    
    if not gold_citations:
        citation_score = 1.0
    else:
        matched_citations = len(gold_citations & pred_citations)
        citation_score = matched_citations / len(gold_citations)

    # 3. Penalty / Financial Damage Arithmetic (30% weight)
    gold_penalty = float(truth.get("penalty_amount", 0.0))
    pred_penalty = float(prediction.get("penalty_amount", 0.0))
    
    if math.isclose(gold_penalty, 0.0, abs_tol=1e-5):
        penalty_score = 1.0 if math.isclose(pred_penalty, 0.0, abs_tol=1e-5) else 0.0
    else:
        relative_err_bps = abs(gold_penalty - pred_penalty) / gold_penalty * 10000.0
        if relative_err_bps <= penalty_tolerance_bps:
            penalty_score = 1.0
        elif relative_err_bps >= (penalty_tolerance_bps * 3):
            penalty_score = 0.0
        else:
            # Linear decay
            decay_range = penalty_tolerance_bps * 2
            penalty_score = max(0.0, (decay_range - (relative_err_bps - penalty_tolerance_bps)) / decay_range)

    composite_score = round(
        (0.40 * verdict_score) + (0.30 * citation_score) + (0.30 * penalty_score),
        4
    )

    return {
        "verdict_score": round(verdict_score, 4),
        "citation_score": round(citation_score, 4),
        "penalty_score": round(penalty_score, 4),
        "composite_score": composite_score,
        "passed": composite_score >= 0.70
    }
