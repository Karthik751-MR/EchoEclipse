# modules/language_detection.py
from langdetect import detect


def detect_language(text):
    """
    Detect the language of the given text using langdetect.

    :param text: The text whose language is to be detected.
    :return: A language code (e.g., "en", "es").
    """
    try:
        return detect(text)
    except Exception as e:
        print("Error detecting language:", e)
        return "en"  # Default to English if detection fails


if __name__ == "__main__":
    sample_text = "Hola, este es un mensaje de prueba."
    print("Detected language:", detect_language(sample_text))
