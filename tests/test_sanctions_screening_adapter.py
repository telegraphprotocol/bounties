"""Unit tests for deterministic SANCTIONS_SCREENING_MATCH evaluator adapter (#190)."""
import unittest
from evaluators.sanctions_screening_adapter import evaluate_sanctions_screening


class TestSanctionsScreeningAdapter(unittest.TestCase):
    def test_exact_sdn_match(self):
        truth = {
            "entity": "BANCO NACIONAL DE CUBA",
            "verdict": "VERDICT: SANCTIONS MATCH (PROHIBITED COUNTERPARTY)",
            "matched": True,
            "uid": "306",
            "program": "CUBA",
            "similarity": 1.00
        }
        prediction = {
            "entity": "BANCO NACIONAL DE CUBA",
            "verdict": "VERDICT: SANCTIONS MATCH",
            "matched": True,
            "uid": "306",
            "program": "CUBA",
            "similarity": 1.00,
            "summary": "VERDICT: SANCTIONS MATCH (PROHIBITED COUNTERPARTY). Exact match found on OFAC SDN List: UID 306, Legal Name 'BANCO NACIONAL DE CUBA', Program [CUBA]."
        }
        res = evaluate_sanctions_screening(truth, prediction)
        self.assertEqual(res["composite_score"], 1.0)
        self.assertTrue(res["passed"])

    def test_clean_vendor_pass(self):
        truth = {
            "entity": "Apple Inc.",
            "verdict": "VERDICT: NO SANCTIONS MATCH (CLEAN COUNTERPARTY)",
            "matched": False,
            "similarity": 0.00
        }
        prediction = {
            "entity": "Apple Inc.",
            "verdict": "VERDICT: NO SANCTIONS MATCH",
            "matched": False,
            "matches_count": 0,
            "similarity": 0.00,
            "summary": "VERDICT: NO SANCTIONS MATCH (CLEAN COUNTERPARTY). Screening 'Apple Inc.' across 19,563 OFAC SDN entries yields 0 matches. Cleared for spend."
        }
        res = evaluate_sanctions_screening(truth, prediction)
        self.assertEqual(res["composite_score"], 1.0)
        self.assertTrue(res["passed"])

    def test_critical_false_negative_penalty(self):
        truth = {
            "entity": "Lazarus Group EVM Address",
            "verdict": "VERDICT: SANCTIONS MATCH (PROHIBITED DIGITAL CURRENCY ADDRESS)",
            "matched": True,
            "address": "0x098b716b8aaf21512996dc57eb0615e2383e2f96"
        }
        # Erroneous clearance of sanctioned wallet: MUST score 0.0
        prediction = {
            "entity": "Lazarus Group EVM Address",
            "verdict": "VERDICT: NO SANCTIONS MATCH",
            "matched": False,
            "summary": "VERDICT: NO SANCTIONS MATCH. Address not found in basic local registry. Payment cleared."
        }
        res = evaluate_sanctions_screening(truth, prediction)
        self.assertEqual(res["composite_score"], 0.0)
        self.assertFalse(res["passed"])
        self.assertIn("CRITICAL_FALSE_NEGATIVE", res.get("breach", ""))

    def test_evm_address_match(self):
        truth = {
            "entity": "Lazarus Group",
            "verdict": "VERDICT: SANCTIONS MATCH",
            "matched": True,
            "address": "0x098b716b8aaf21512996dc57eb0615e2383e2f96",
            "program": "DPRK"
        }
        prediction = {
            "entity": "Lazarus Group",
            "verdict": "VERDICT: SANCTIONS MATCH",
            "matched": True,
            "address": "0x098B716B8Aaf21512996dC57EB0615e2383E2f96",
            "program": "DPRK",
            "summary": "VERDICT: SANCTIONS MATCH (PROHIBITED DIGITAL CURRENCY ADDRESS). Identified OFAC SDN digital currency address 0x098B716B8Aaf21512996dC57EB0615e2383E2f96 under DPRK sanctions program."
        }
        res = evaluate_sanctions_screening(truth, prediction)
        self.assertEqual(res["composite_score"], 1.0)
        self.assertTrue(res["passed"])


if __name__ == "__main__":
    unittest.main()
