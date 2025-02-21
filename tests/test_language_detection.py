# tests/test_language_detection.py
import unittest
from src.modules.language_detection import detect_language


class TestLanguageDetection(unittest.TestCase):
    def test_detect_english(self):
        text = "This is a test message."
        language = detect_language(text)
        self.assertEqual(language, "en")

    def test_detect_spanish(self):
        text = "Este es un mensaje de prueba."
        language = detect_language(text)
        self.assertEqual(language, "es")


if __name__ == "__main__":
    unittest.main()
