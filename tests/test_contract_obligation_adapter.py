"""Unit tests for deterministic CONTRACT_OBLIGATION evaluator adapter (#192)."""
import unittest
from evaluators.contract_obligation_adapter import evaluate_contract_obligation


class TestContractObligationAdapter(unittest.TestCase):
    def test_perfect_match(self):
        truth = {
            "verdict": "DELAY_PENALTY",
            "citations": ["MahaRERA Section 18", "Clause 14(b)"],
            "penalty_amount": 11550.00
        }
        prediction = {
            "verdict": "DELAY_PENALTY",
            "citations": ["maharera section 18", "clause 14(b)"],
            "penalty_amount": 11550.00
        }
        res = evaluate_contract_obligation(truth, prediction)
        self.assertEqual(res["composite_score"], 1.0)
        self.assertTrue(res["passed"])

    def test_verdict_mismatch(self):
        truth = {
            "verdict": "BREACH",
            "citations": ["FIDIC Sub-Clause 20.1"],
            "penalty_amount": 50000.00
        }
        prediction = {
            "verdict": "COMPLIANT",
            "citations": ["FIDIC Sub-Clause 20.1"],
            "penalty_amount": 50000.00
        }
        res = evaluate_contract_obligation(truth, prediction)
        self.assertEqual(res["verdict_score"], 0.0)
        self.assertEqual(res["composite_score"], 0.60)
        self.assertFalse(res["passed"])

    def test_penalty_tolerance_decay(self):
        truth = {
            "verdict": "DELAY_PENALTY",
            "citations": ["MSMED Act Section 16"],
            "penalty_amount": 1000.00
        }
        # 1.5% error = 150 bps error (tolerance = 100 bps)
        prediction = {
            "verdict": "DELAY_PENALTY",
            "citations": ["MSMED Act Section 16"],
            "penalty_amount": 1015.00
        }
        res = evaluate_contract_obligation(truth, prediction, penalty_tolerance_bps=100)
        self.assertEqual(res["verdict_score"], 1.0)
        self.assertEqual(res["citation_score"], 1.0)
        self.assertGreater(res["penalty_score"], 0.0)
        self.assertTrue(res["passed"])


if __name__ == "__main__":
    unittest.main()
