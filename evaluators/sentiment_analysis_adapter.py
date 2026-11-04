"""Deterministic SENTIMENT_ANALYSIS evaluator adapter (#152)."""
from __future__ import annotations
from typing import Sequence

VALID_POLARITIES = frozenset({"positive", "neutral", "negative"})


def evaluate_sentiment_predictions(
    gold_polarities: Sequence[str],
    predicted_polarities: Sequence[str],
) -> dict[str, float]:
    if len(gold_polarities) != len(predicted_polarities) or not gold_polarities:
        raise ValueError("Inputs must be non-empty and match in length")

    norm_gold = [str(g).strip().lower() for g in gold_polarities]
    norm_pred = [str(p).strip().lower() for p in predicted_polarities]

    total = len(norm_gold)
    exact = sum(1 for g, p in zip(norm_gold, norm_pred) if g == p)
    return {
        "samples": float(total),
        "accuracy": round(exact / total, 6),
    }
