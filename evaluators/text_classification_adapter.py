"""Deterministic TEXT_CLASSIFICATION evaluator adapter computing accuracy and macro-F1 (#154)."""
from __future__ import annotations
from typing import Iterable, Mapping, Sequence


def evaluate_text_classification(
    gold_labels: Sequence[str],
    predicted_labels: Sequence[str],
) -> dict[str, float]:
    if len(gold_labels) != len(predicted_labels) or not gold_labels:
        raise ValueError("gold_labels and predicted_labels must be non-empty and equal length")

    n = len(gold_labels)
    correct = sum(1 for g, p in zip(gold_labels, predicted_labels) if g == p)
    accuracy = correct / n

    classes = sorted(set(gold_labels) | set(predicted_labels))
    f1_scores = []
    for cls in classes:
        tp = sum(1 for g, p in zip(gold_labels, predicted_labels) if g == cls and p == cls)
        fp = sum(1 for g, p in zip(gold_labels, predicted_labels) if g != cls and p == cls)
        fn = sum(1 for g, p in zip(gold_labels, predicted_labels) if g == cls and p != cls)
        denom = 2 * tp + fp + fn
        f1_scores.append((2 * tp / denom) if denom > 0 else 0.0)

    macro_f1 = sum(f1_scores) / len(classes) if classes else 0.0
    return {
        "samples": float(n),
        "accuracy": round(accuracy, 6),
        "macro_f1": round(macro_f1, 6),
    }
