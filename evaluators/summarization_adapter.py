"""Deterministic SUMMARIZATION ROUGE-1 evaluator adapter (#151)."""
from __future__ import annotations
from collections import Counter


def rouge1_f1(reference: str, candidate: str) -> float:
    ref_tokens = reference.lower().split()
    cand_tokens = candidate.lower().split()
    if not ref_tokens or not cand_tokens:
        return 0.0
    overlap = sum((Counter(ref_tokens) & Counter(cand_tokens)).values())
    prec = overlap / len(cand_tokens)
    rec = overlap / len(ref_tokens)
    return round((2 * prec * rec / (prec + rec)), 6) if (prec + rec) > 0 else 0.0
