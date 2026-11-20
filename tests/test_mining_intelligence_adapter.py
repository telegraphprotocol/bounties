"""Unit tests for deterministic MINING_INTELLIGENCE and MINING_RESERVE evaluator adapter (#200)."""
import unittest
from evaluators.mining_intelligence_adapter import evaluate_mining_intelligence


class TestMiningIntelligenceAdapter(unittest.TestCase):
    def test_mount_morgan_perfect_match(self):
        truth = {
            "entity": "Mount Morgan Mine",
            "verdict": "VERIFIED_HISTORICAL_RECORD",
            "production_tonnes_gold": 262.0,
            "geology": "VHMS (Volcanic-Hosted Massive Sulfide)",
            "authority": "Geological Survey of Queensland (GSQ)"
        }
        prediction = {
            "entity": "Mount Morgan Mine",
            "verdict": "VERIFIED_HISTORICAL_RECORD",
            "production_tonnes_gold": 262.0,
            "geology": "Subvolcanic VHMS pipe trondhjemite",
            "authority": "Queensland Department of Resources / GSQ",
            "summary": "Historic VHMS pipe deposit verified against GSQ records producing 262 tonnes gold."
        }
        res = evaluate_mining_intelligence(truth, prediction)
        self.assertGreaterEqual(res["composite_score"], 0.85)
        self.assertTrue(res["passed"])

    def test_kalgoorlie_super_pit_acceptable_variance(self):
        truth = {
            "entity": "Kalgoorlie Super Pit",
            "verdict": "VERIFIED_HISTORICAL_RECORD",
            "production_tonnes_gold": 1860.0,
            "geology": "Orogenic Mesothermal Quartz",
            "authority": "Geological Survey of Western Australia (GSWA)"
        }
        # 1.5% variance = 150 bps error (tolerance = 500 bps)
        prediction = {
            "entity": "Kalgoorlie Super Pit",
            "verdict": "VERIFIED_HISTORICAL_RECORD",
            "production_tonnes_gold": 1880.0,
            "geology": "Archean orogenic quartz-vein system",
            "authority": "GSWA Open File",
            "summary": "Golden Mile orogenic deposit yielding ~1880 tonnes gold under GSWA records."
        }
        res = evaluate_mining_intelligence(truth, prediction, metric_tolerance_bps=500)
        self.assertEqual(res["entity_score"], 1.0)
        self.assertEqual(res["metric_score"], 1.0)
        self.assertTrue(res["passed"])

    def test_hallucinated_deposit_rejection(self):
        truth = {
            "entity": "Carlin Trend",
            "verdict": "VERIFIED_HISTORICAL_RECORD",
            "production_tonnes_gold": 2600.0,
            "geology": "Sediment-Hosted Disseminated Gold",
            "authority": "United States Geological Survey (USGS)"
        }
        # Gross hallucination: wrong geology, impossible metrics, no authority
        prediction = {
            "entity": "Carlin Trend",
            "verdict": "UNVERIFIED_ESTIMATE",
            "production_tonnes_gold": 50.0,
            "geology": "Alluvial River Placer Gravels",
            "authority": "Random Blog Post",
            "summary": "Small placer deposit estimated at 50 tonnes."
        }
        res = evaluate_mining_intelligence(truth, prediction)
        self.assertLess(res["composite_score"], 0.50)
        self.assertFalse(res["passed"])

    def test_unindexed_deposit(self):
        truth = {
            "entity": "Atlantis Submarine Seamount Gold",
            "unindexed": True
        }
        prediction = {
            "entity": "Atlantis Submarine Seamount Gold",
            "verdict": "UNINDEXED_SITE",
            "summary": "Deposit not cataloged in official national geological surveys."
        }
        res = evaluate_mining_intelligence(truth, prediction)
        self.assertEqual(res["composite_score"], 1.0)
        self.assertTrue(res["passed"])


if __name__ == "__main__":
    unittest.main()
