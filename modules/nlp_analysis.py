from textblob import TextBlob

# Define scam keywords for multiple languages
scam_keywords = {
    "en": ["urgent", "account number", "payment", "fraud", "transfer", "verification"],
    "hi": ["तत्काल", "खाता संख्या", "भुगतान", "धोखाधड़ी", "स्थानांतरण", "सत्यापन"],
    "es": [
        "urgente",
        "número de cuenta",
        "pago",
        "fraude",
        "transferencia",
        "verificación",
    ],
    "fr": [
        "urgent",
        "numéro de compte",
        "paiement",
        "fraude",
        "transfert",
        "vérification",
    ],
    "te": ["అత్యవసరం", "ఖాతా సంఖ్య", "చెల్లింపు", "మోసం", "బదిలీ", "ధృవీకరణ"],
    "en-in": [
        "urgent",
        "account number",
        "payment",
        "fraud",
        "transfer",
        "verification",
    ],
}


def detect_keywords(text, language="en"):
    """
    Detect scam keywords in the text based on the language.

    Args:
        text (str): The text to analyze.
        language (str): The language code (e.g., "en", "hi", "es", "fr", "te", "en-in").

    Returns:
        list: List of detected keywords.
    """
    keywords = scam_keywords.get(language, scam_keywords["en"])
    found = [word for word in keywords if word.lower() in text.lower()]
    return found


def analyze_sentiment(text):
    """
    Analyze the sentiment of the text.

    Args:
        text (str): The text to analyze.

    Returns:
        float: Sentiment polarity score between -1 (negative) and 1 (positive).
    """
    blob = TextBlob(text)
    return blob.sentiment.polarity
