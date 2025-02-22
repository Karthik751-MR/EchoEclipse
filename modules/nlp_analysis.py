from textblob import TextBlob

# Define scam keywords for multiple languages
scam_keywords = {
    "en": ["urgent", "account number", "payment", "fraud", "transfer", "verification"],
    "es": ["urgente", "número de cuenta", "pago", "fraude"],
}


def detect_keywords(text, language="en"):
    keywords = scam_keywords.get(language, scam_keywords["en"])
    found = [word for word in keywords if word.lower() in text.lower()]
    return found


def analyze_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity  # score between -1 (negative) and 1 (positive)
