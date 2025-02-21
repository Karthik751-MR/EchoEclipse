# tests/test_risk_scoring.py
import unittest
from src.modules.risk_scoring import calculate_risk_score


class TestRiskScoring(unittest.TestCase):
    def test_risk_score(self):
        transcript = "Your bank requires urgent confirmation of your account number."
        metadata = {"hour": 23}
        score, keywords = calculate_risk_score(
            transcript,
            language="en",
            metadata=metadata,
            caller_number="+18001234567",
            voice_match=False,
        )
        self.assertTrue(0 <= score <= 100)
        self.assertIsInstance(keywords, list)


if __name__ == "__main__":
    unittest.main()
