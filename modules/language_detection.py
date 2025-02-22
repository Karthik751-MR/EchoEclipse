from langdetect import detect, DetectorFactory
import logging

# For reproducible results
DetectorFactory.seed = 0


def detect_language(text, default_language="en"):
    """
    Detect the language of the given text.

    Args:
        text (str): The text to analyze.
        default_language (str): The default language to return if detection fails.

    Returns:
        str: Detected language code (e.g., "en", "hi", "es", "fr").
    """
    try:
        # Detect the language
        language = detect(text)
        # Map detected language to supported languages
        supported_languages = {"en", "hi", "es", "fr", "te"}
        return language if language in supported_languages else default_language
    except Exception as e:
        # Log the error for debugging
        logging.error(f"Error detecting language: {e}")
        return default_language  # Return the default language if detection fails
