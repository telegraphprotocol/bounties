"""Unit tests for GRID_POWER_PRICE evaluator adapter (Missions 11, 12 #199, #200)."""
from __future__ import annotations
import unittest
from evaluators.grid_power_price_adapter import (
    evaluate_grid_power_price,
    _extract_lmp_price,
    _extract_market,
)


class TestGridPowerPriceAdapter(unittest.TestCase):

    def test_price_extraction_helpers(self):
        """Verify extraction of numeric LMP price from various field shapes and summaries."""
        self.assertEqual(_extract_lmp_price({"lmp_usd_per_mwh": 38.09459}), 38.09459)
        self.assertEqual(_extract_lmp_price({"price_mwh": 41.2}), 41.2)
        self.assertEqual(_extract_lmp_price({"summary": "Settlement price is $41.20/MWh at NP15"}), 41.20)
        self.assertEqual(_extract_lmp_price({"summary": "Curtailment negative LMP -$12.50 USD/MWh"}), -12.50)

    def test_caiso_np15_accurate_settlement(self):
        """Verify evaluation of authentic CAISO NP15 wholesale settlement."""
        truth = {
            "node_or_zone": "CAISO NP15",
            "lmp_usd_per_mwh": 41.20,
            "market": "RTM",
            "interval_start": "2026-11-20T10:00:00Z"
        }
        prediction = {
            "node_or_zone": "NP15 (North of Path 15)",
            "lmp_usd_per_mwh": 41.20,
            "market": "RTM",
            "interval_start": "2026-11-20T10:00:00Z",
            "summary": "GRID POWER PRICE: CAISO NP15 (North of Path 15) Real-Time Market LMP settlement verified at $41.20/MWh.",
            "provenance": "CAISO OASIS Settlement Feed"
        }
        result = evaluate_grid_power_price(truth, prediction)
        self.assertTrue(result["passed"])
        self.assertGreaterEqual(result["composite_score"], 0.95)
        self.assertEqual(result["price_score"], 1.0)
        self.assertEqual(result["node_score"], 1.0)

    def test_ercot_houston_hub_settlement(self):
        """Verify evaluation of authentic ERCOT Houston hub settlement."""
        truth = {
            "node_or_zone": "ERCOT Houston Hub",
            "lmp_usd_per_mwh": 34.20,
            "market": "DAM",
            "interval_start": "2026-11-20T00:00:00Z"
        }
        prediction = {
            "hub": "ERCOT Houston Hub",
            "price_mwh": 34.20,
            "market": "Day-Ahead",
            "interval_start": "2026-11-20T00:00:00Z",
            "summary": "GRID POWER PRICE: ERCOT Houston Hub Day-Ahead Market LMP settlement verified at $34.20/MWh.",
            "provenance": "ERCOT Settlement Point Price (SPP) API"
        }
        result = evaluate_grid_power_price(truth, prediction)
        self.assertTrue(result["passed"])
        self.assertGreaterEqual(result["composite_score"], 0.95)
        self.assertEqual(result["price_score"], 1.0)

    def test_inverted_price_curtailment_penalty(self):
        """Verify that sign inversion (positive vs negative pricing) fails price gate."""
        truth = {
            "node_or_zone": "CAISO ZP26",
            "lmp_usd_per_mwh": -15.00,  # Negative pricing during renewable curtailment
            "market": "RTM"
        }
        pred = {
            "node_or_zone": "CAISO ZP26",
            "lmp_usd_per_mwh": 15.00,   # Erroneous positive sign
            "market": "RTM"
        }
        result = evaluate_grid_power_price(truth, pred)
        self.assertEqual(result["price_score"], 0.0)
        self.assertFalse(result["passed"])

    def test_excessive_price_variance(self):
        """Verify that price deviation > 30% receives 0 price credit."""
        truth = {
            "node_or_zone": "CAISO SP15",
            "lmp_usd_per_mwh": 40.00,
            "market": "RTM"
        }
        pred = {
            "node_or_zone": "CAISO SP15",
            "lmp_usd_per_mwh": 75.00,  # 87.5% error
            "market": "RTM"
        }
        result = evaluate_grid_power_price(truth, pred)
        self.assertEqual(result["price_score"], 0.0)
        self.assertFalse(result["passed"])


if __name__ == "__main__":
    unittest.main()
