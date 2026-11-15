"""Deterministic TRANSLATION character n-gram overlap evaluator adapter (#153)."""
from __future__ import annotations
from collections import Counter


def char_ngram_f1(reference: str, hypothesis: str, n: int = 4) -> float:
    ref = reference.strip()
    hyp = hypothesis.strip()
    if len(ref) < n or len(hyp) < n:
        return 1.0 if ref == hyp and ref else 0.0
    ref_ngrams = Counter(ref[i : i + n] for i in range(len(ref) - n + 1))
    hyp_ngrams = Counter(hyp[i : i + n] for i in range(len(hyp) - n + 1))
    overlap = sum((ref_ngrams & hyp_ngrams).values())
    prec = overlap / sum(hyp_ngrams.values())
    rec = overlap / sum(ref_ngrams.values())
    return round((2 * prec * rec / (prec + rec)), 6) if (prec + rec) > 0 else 0.0
