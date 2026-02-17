from modules.language_detection import detect_language


def test_detects_english_text():
    assert detect_language("Please verify your account immediately") == "en"


def test_returns_default_for_empty_input():
    assert detect_language("", default_language="en") == "en"
