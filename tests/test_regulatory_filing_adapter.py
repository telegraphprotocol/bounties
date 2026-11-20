"""Unit tests for REGULATORY_FILING_MONITOR evaluator adapter (Mission 04 & 13 #192, #201)."""
from __future__ import annotations
import unittest
from evaluators.regulatory_filing_adapter import (
    evaluate_regulatory_filing,
    validate_edgar_accession,
    is_official_regulatory_url,
)


class TestRegulatoryFilingAdapter(unittest.TestCase):

    def test_edgar_accession_validation(self):
        """Verify SEC EDGAR 18-character accession number syntax."""
        valid_accession = "0000320193-24-000106"
        self.assertTrue(validate_edgar_accession(valid_accession))

        # Invalid formats
        self.assertFalse(validate_edgar_accession("000032019324000106"))  # Missing hyphens
        self.assertFalse(validate_edgar_accession("320193-24-106"))       # Insufficient digits
        self.assertFalse(validate_edgar_accession("INVALID-ACCESSION"))

    def test_official_regulatory_url_domain_guard(self):
        """Verify domain whitelist filtering for primary government registers."""
        sec_url = "https://www.sec.gov/Archives/edgar/data/320193/000032019324000106/aapl-20240928.htm"
        fed_url = "https://www.federalregister.gov/documents/2026/02/14/2026-03120/airworthiness-directives-boeing"
        blog_url = "https://unverified-trader-blog.com/leaked-filings/tesla"

        self.assertTrue(is_official_regulatory_url(sec_url))
        self.assertTrue(is_official_regulatory_url(fed_url))
        self.assertFalse(is_official_regulatory_url(blog_url))

    def test_authentic_sec_edgar_filing_evaluation(self):
        """Verify evaluation of accurate SEC EDGAR 10-K and 10-Q filings."""
        truth = {
            "entity": "Apple Inc.",
            "filing_count": 4,
            "forms": ["10-K", "10-Q"],
            "period": "last 12 months"
        }
        prediction = {
            "entity": "Apple Inc.",
            "filing_count": 4,
            "filings": [
                {
                    "form": "10-K",
                    "filingDate": "2024-11-01",
                    "accessionNumber": "0000320193-24-000106",
                    "url": "https://www.sec.gov/Archives/edgar/data/320193/000032019324000106/aapl-20240928.htm"
                },
                {
                    "form": "10-Q",
                    "filingDate": "2025-02-01",
                    "accessionNumber": "0000320193-25-000008",
                    "url": "https://www.sec.gov/Archives/edgar/data/320193/000032019325000008/aapl-20241228.htm"
                }
            ],
            "urls": [
                "https://www.sec.gov/Archives/edgar/data/320193/000032019324000106/aapl-20240928.htm",
                "https://www.sec.gov/Archives/edgar/data/320193/000032019325000008/aapl-20241228.htm"
            ],
            "summary": "FILING MONITOR STATUS: ACTIVE FILER (SEC EDGAR). Identified 4 statutory filings for Apple Inc. across period last 12 months (Forms 10-K, 10-Q).",
            "provenance": "SEC EDGAR Submissions API (data.sec.gov)"
        }
        result = evaluate_regulatory_filing(truth, prediction)
        self.assertTrue(result["passed"])
        self.assertGreaterEqual(result["composite_score"], 0.95)
        self.assertEqual(result["count_score"], 1.0)
        self.assertEqual(result["form_score"], 1.0)
        self.assertEqual(result["url_score"], 1.0)

    def test_federal_register_rule_monitoring(self):
        """Verify Federal Register agency rulemaking monitor evaluation."""
        truth = {
            "entity": "Boeing",
            "filing_count": 180,
            "forms": ["Rule", "Notice", "Proposed Rule"]
        }
        prediction = {
            "entity": "Boeing",
            "filing_count": 180,
            "summary": "Identified 180 Federal Register documents mentioning Boeing by FAA: 75 Rules, 58 Notices, 47 Proposed Rules.",
            "urls": ["https://www.federalregister.gov/documents/search?conditions%5Bterm%5D=boeing"],
            "provenance": "US Federal Register API"
        }
        result = evaluate_regulatory_filing(truth, prediction)
        self.assertTrue(result["passed"])
        self.assertGreaterEqual(result["composite_score"], 0.90)

    def test_zero_filings_non_filer(self):
        """Verify handling of inactive entities with zero statutory filings."""
        truth = {
            "entity": "Private Shell Co",
            "filing_count": 0
        }
        prediction = {
            "entity": "Private Shell Co",
            "filing_count": 0,
            "summary": "No statutory SEC filings or Federal Register disclosures found for Private Shell Co in requested period.",
            "urls": []
        }
        result = evaluate_regulatory_filing(truth, prediction)
        self.assertTrue(result["passed"])
        self.assertEqual(result["composite_score"], 1.0)


if __name__ == "__main__":
    unittest.main()
