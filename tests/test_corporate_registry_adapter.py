"""Unit tests for CORPORATE_REGISTRY_LOOKUP evaluator adapter (Mission 03 #191)."""
from __future__ import annotations
import unittest
from evaluators.corporate_registry_adapter import (
    evaluate_corporate_registry,
    validate_iso17442_lei,
)


class TestCorporateRegistryAdapter(unittest.TestCase):

    def test_iso17442_lei_checksum(self):
        """Verify ISO 17442 MOD 97-10 checksum validation."""
        # Valid official LEIs from GLEIF Global LEI Index
        tesla_lei = "54930043XZGB27CTOV49"
        stripe_lei = "549300CLHGIPTCYHQ143"
        sap_lei = "529900D6BF99LW9R2E68"
        self.assertTrue(validate_iso17442_lei(tesla_lei))
        self.assertTrue(validate_iso17442_lei(stripe_lei))
        self.assertTrue(validate_iso17442_lei(sap_lei))

        # Corrupted / invalid check digits
        corrupted_lei = "54930043XZGB27CTOV00"
        self.assertFalse(validate_iso17442_lei(corrupted_lei))
        self.assertFalse(validate_iso17442_lei("SHORTLEI123"))
        self.assertFalse(validate_iso17442_lei("54930043XZGB27CTOV4X"))  # Non-numeric check digits

    def test_valid_corporate_resolution(self):
        """Verify accurate corporate registration resolution matches with high score."""
        truth = {
            "legal_name": "TESLA, INC.",
            "registration_id": "54930043XZGB27CTOV49",
            "active": True,
            "jurisdiction": "US-DE",
            "found": True
        }
        pred = {
            "legal_name": "Tesla, Inc.",
            "registration_id": "54930043XZGB27CTOV49",
            "active": True,
            "jurisdiction": "US-DE",
            "summary": "Verified active registration for Tesla, Inc. under Delaware Division of Corporations and GLEIF LEI Index (54930043XZGB27CTOV49).",
            "provenance": "GLEIF Global LEI Index / Delaware Division of Corporations"
        }
        result = evaluate_corporate_registry(truth, pred)
        self.assertTrue(result["passed"])
        self.assertGreaterEqual(result["composite_score"], 0.95)
        self.assertEqual(result["status_score"], 1.0)
        self.assertEqual(result["identifier_score"], 1.0)

    def test_lapsed_registration_penalty(self):
        """Verify that false-positive active clearance on a lapsed LEI is caught and penalized."""
        truth = {
            "legal_name": "Old Trading Corp",
            "registration_id": "529900EXAMPLELAPSED11",
            "active": False,
            "jurisdiction": "GB",
            "found": True,
            "status": "lapsed"
        }
        # Erroneous prediction claiming active
        pred_bad = {
            "legal_name": "Old Trading Corp Ltd",
            "registration_id": "529900EXAMPLELAPSED11",
            "active": True,
            "jurisdiction": "GB",
            "summary": "Entity is active and approved for clearing."
        }
        result_bad = evaluate_corporate_registry(truth, pred_bad)
        self.assertLess(result_bad["status_score"], 0.20)
        self.assertFalse(result_bad["passed"])

        # Correct prediction flagging lapsed status
        pred_good = {
            "legal_name": "Old Trading Corp",
            "registration_id": "529900EXAMPLELAPSED11",
            "active": False,
            "jurisdiction": "GB",
            "summary": "VERDICT: LAPSED REGISTRATION. Entity LEI registration lapsed without statutory renewal under GLEIF.",
            "provenance": "GLEIF LEI Index"
        }
        result_good = evaluate_corporate_registry(truth, pred_good)
        self.assertTrue(result_good["passed"])
        self.assertGreaterEqual(result_good["composite_score"], 0.90)

    def test_unregistered_entity_resolution(self):
        """Verify handling of unindexed or fictitious entities."""
        truth = {
            "legal_name": "Nonexistent Fake Company 12345",
            "found": False,
            "active": False
        }
        pred = {
            "found": False,
            "active": False,
            "summary": "No statutory corporate record found in national registries or GLEIF.",
            "provenance": "Companies House / GLEIF"
        }
        result = evaluate_corporate_registry(truth, pred)
        self.assertTrue(result["passed"])
        self.assertEqual(result["composite_score"], 1.0)


if __name__ == "__main__":
    unittest.main()
