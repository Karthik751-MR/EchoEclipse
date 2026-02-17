import logging

from modules.caller_verification import is_trusted_number
from modules.nlp_analysis import analyze_sentiment, detect_keywords

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


def calculate_risk_score(
    transcript,
    language="en",
    metadata=None,
    caller_number=None,
    keywords=None,
    sentiment_score=None,
    voice_match=False,
):
    """Calculate a risk score and return (score, detected_keywords)."""
    try:
        detected_keywords = keywords if keywords is not None else detect_keywords(transcript, language)
        keyword_score = len(detected_keywords) * 20

        computed_sentiment = (
            sentiment_score if sentiment_score is not None else analyze_sentiment(transcript)
        )
        sentiment_score_risk = 20 if computed_sentiment < 0 else 0

        metadata_score = (
            10
            if metadata and (metadata.get("hour", 12) < 6 or metadata.get("hour", 12) > 22)
            else 0
        )

        caller_score = -30 if caller_number and is_trusted_number(caller_number) else 0
        voice_score = -20 if voice_match else 0

        total_score = keyword_score + sentiment_score_risk + metadata_score + caller_score + voice_score
        total_score = max(0, min(100, total_score))

        return total_score, detected_keywords
    except Exception as exc:
        logging.error("Error calculating risk score: %s", exc)
        return 0, []
