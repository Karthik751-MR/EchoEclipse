# modules/nlp_analysis.py
from transformers import pipeline

# Define scam keywords for English and Spanish.
scam_keywords = {
    "en": ["urgent", "account number", "payment", "fraud"],
    "es": ["urgente", "número de cuenta", "pago", "fraude"],
}


def detect_keywords(text, language="en"):
    """
    Detect scam-related keywords in the text.

    :param text: The input text.
    :param language: The language code of the text.
    :return: A list of found keywords.
    """
    keywords = scam_keywords.get(language, scam_keywords["en"])
    found = [word for word in keywords if word.lower() in text.lower()]
    return found


# Set up a sentiment analysis pipeline using Hugging Face Transformers.
sentiment_pipeline = pipeline("sentiment-analysis")


def analyze_sentiment(text):
    """
    Analyze the sentiment of the given text.

    :param text: The input text.
    :return: A list containing sentiment analysis results.
    """
    result = sentiment_pipeline(text)
    return result


if __name__ == "__main__":
    text = "Your bank requires urgent confirmation of your account number."
    print("Detected Keywords:", detect_keywords(text, language="en"))
    print("Sentiment Analysis:", analyze_sentiment(text))
