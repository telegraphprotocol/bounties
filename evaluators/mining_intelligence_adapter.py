"""Deterministic MINING_INTELLIGENCE and MINING_RESERVE evaluator adapter for Mission 12 Mining & Power (#200).

Evaluates mining and geological intelligence predictions against authoritative survey ground truth:
1. Deposit entity verification & status match (30% weight)
2. Production metrics arithmetic accuracy within basis-point tolerance (30% weight)
3. Geological deposit classification precision (20% weight)
4. Authoritative geological survey citation recall (20% weight)
"""
from __future__ import annotations
import math
import re
from typing import Any, Mapping


def evaluate_mining_intelligence(
    truth: Mapping[str, Any],
    prediction: Mapping[str, Any],
    metric_tolerance_bps: int = 500
) -> dict[str, float | bool | str]:
    """Score a miner or agent output against mining intelligence ground truth.
    
    Returns a deterministic dictionary containing component scores and composite score [0.0, 1.0].
    """
    # 0. Hallucination Guard
    pred_summary = str(prediction.get("summary", "") or prediction.get("explanation", ""))
    pred_verdict = str(prediction.get("verdict", "") or prediction.get("status", "")).strip().upper()
    gold_verdict = str(truth.get("verdict", "") or truth.get("status", "")).strip().upper()

    # Check for obvious negative status or unindexed
    if truth.get("unindexed", False):
        unindexed_match = 1.0 if "UNINDEXED" in pred_verdict or "NOT_FOUND" in pred_verdict else 0.0
        return {
            "entity_score": unindexed_match,
            "metric_score": 1.0 if unindexed_match else 0.0,
            "geology_score": 1.0 if unindexed_match else 0.0,
            "authority_score": 1.0 if unindexed_match else 0.0,
            "composite_score": unindexed_match,
            "passed": unindexed_match >= 0.70
        }

    # 1. Entity & Verdict Verification (30% weight)
    gold_entity = str(truth.get("entity", "") or truth.get("site", "")).strip().lower()
    pred_entity = str(prediction.get("entity", "") or prediction.get("site", "")).strip().lower()
    
    entity_matched = (gold_entity == pred_entity) or (gold_entity in pred_summary.lower()) if gold_entity else True
    verdict_matched = (gold_verdict == pred_verdict) if gold_verdict else True
    
    entity_score = 1.0 if (entity_matched and verdict_matched) else (0.5 if entity_matched else 0.0)

    # 2. Production Metrics Accuracy (30% weight)
    gold_production = float(truth.get("production_tonnes_gold", 0.0) or truth.get("metric_value", 0.0))
    pred_production = float(prediction.get("production_tonnes_gold", 0.0) or prediction.get("metric_value", 0.0))

    if pred_production == 0.0 and pred_summary:
        # Extract from text if omitted in structured fields
        m = re.search(r'(\d+(?:\.\d+)?)\s*(?:tonnes?|t\b|million\s*oz|m\s*oz)', pred_summary, re.IGNORECASE)
        if m:
            pred_production = float(m.group(1))

    if math.isclose(gold_production, 0.0, abs_tol=1e-5):
        metric_score = 1.0 if math.isclose(pred_production, 0.0, abs_tol=1e-5) else 0.5
    else:
        rel_error_bps = abs(gold_production - pred_production) / gold_production * 10000.0
        if rel_error_bps <= metric_tolerance_bps:
            metric_score = 1.0
        elif rel_error_bps >= (metric_tolerance_bps * 3):
            metric_score = 0.0
        else:
            decay_range = metric_tolerance_bps * 2
            metric_score = max(0.0, (decay_range - (rel_error_bps - metric_tolerance_bps)) / decay_range)

    # 3. Geological Classification Matching (20% weight)
    gold_geology = str(truth.get("geology", "") or truth.get("classification", "")).strip().lower()
    pred_geology = str(prediction.get("geology", "") or prediction.get("classification", "")).strip().lower()
    
    if not gold_geology:
        geology_score = 1.0
    else:
        # Match keywords like vhms, orogenic, carlin, placer, epithermal, porphyry
        geology_keywords = [w for w in re.split(r'[\s,/()\-]+', gold_geology) if len(w) > 3]
        if not geology_keywords:
            geology_score = 1.0 if gold_geology in pred_geology or gold_geology in pred_summary.lower() else 0.0
        else:
            matches = sum(1 for kw in geology_keywords if kw in pred_geology or kw in pred_summary.lower())
            geology_score = round(matches / len(geology_keywords), 2)

    # 4. Authoritative Registry / Survey Citation Recall (20% weight)
    gold_authority = str(truth.get("authority", "") or truth.get("source", "")).strip().lower()
    pred_authority = str(prediction.get("authority", "") or prediction.get("source", "")).strip().lower()

    if not gold_authority:
        authority_score = 1.0
    else:
        auth_keywords = [w for w in re.split(r'[\s,/()\-]+', gold_authority) if len(w) > 2]
        matches = sum(1 for kw in auth_keywords if kw in pred_authority or kw in pred_summary.lower())
        authority_score = 1.0 if matches > 0 else 0.0

    composite_score = round(
        (0.30 * entity_score) + (0.30 * metric_score) + (0.20 * geology_score) + (0.20 * authority_score),
        4
    )

    return {
        "entity_score": round(entity_score, 4),
        "metric_score": round(metric_score, 4),
        "geology_score": round(geology_score, 4),
        "authority_score": round(authority_score, 4),
        "composite_score": composite_score,
        "passed": composite_score >= 0.70
    }
