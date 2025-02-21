# tests/test_nlp_analysis.py
import unittest
from src.modules.nlp_analysis import detect_keywords, analyze_sentiment


class TestNLPAnalysis(unittest.TestCase):
    def test_detect_keywords(self):
        text = "Your bank requires urgent confirmation of your account number."
        keywords = detect_keywords(text, language="en")
        # Expecting at least one keyword from our dictionary (e.g., "urgent")
        self.assertTrue(len(keywords) > 0)
        self.assertIn("urgent", [word.lower() for word in keywords])

    def test_analyze_sentiment(self):
        text = "I hate waiting for my money."
        result = analyze_sentiment(text)
        # Check that the sentiment result is a list with a dict that contains 'label'
        self.assertTrue(isinstance(result, list))
        self.assertTrue("label" in result[0])


if __name__ == "__main__":
    unittest.main()
