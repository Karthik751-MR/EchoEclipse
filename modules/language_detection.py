from langdetect import detect, DetectorFactory

# For reproducible results
DetectorFactory.seed = 0


def detect_language(text):
    try:
        return detect(text)
    except Exception as e:
        # Log error if needed
        return "en"  # Default to English if detection fails
