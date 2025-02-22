from modules.nlp_analysis import detect_keywords, analyze_sentiment
from modules.caller_verification import is_trusted_number
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def calculate_risk_score(
    transcript,
    language="en",
    metadata=None,
    caller_number=None,
    keywords=None,
    sentiment_score=None,
    voice_match=False,
):
    """
    Calculate the risk score for a call based on various factors.

    Args:
        transcript (str): The transcribed text of the call.
        language (str): The language of the transcript (e.g., "en", "hi", "es", "fr", "te").
        metadata (dict): Additional metadata about the call (e.g., call time).
        caller_number (str): The caller's phone number.
        keywords (list): List of detected scam keywords.
        sentiment_score (float): The sentiment score of the transcript.
        voice_match (bool): Whether the caller's voice matches a trusted profile.

    Returns:
        int: The calculated risk score.
    """
    try:
        # 1. Keyword score: each keyword adds 20 points
        if keywords is None:
            keywords = detect_keywords(transcript, language)
        keyword_score = len(keywords) * 20

        # 2. Sentiment score: add 20 points if sentiment is negative
        if sentiment_score is None:
            sentiment_score = analyze_sentiment(transcript)
        sentiment_score_risk = 20 if sentiment_score < 0 else 0

        # 3. Metadata score: add 10 points for calls during odd hours (<6AM or >10PM)
        metadata_score = (
            10
            if metadata
            and (metadata.get("hour", 12) < 6 or metadata.get("hour", 12) > 22)
            else 0
        )

        # 4. Caller adjustment: subtract 30 points if caller is trusted
        caller_score = -30 if caller_number and is_trusted_number(caller_number) else 0

        # 5. Voice biometrics: subtract 20 points if voice matches trusted profile
        voice_score = -20 if voice_match else 0

        # 6. Total risk score (clamped between 0 and 100)
        total_score = (
            keyword_score
            + sentiment_score_risk
            + metadata_score
            + caller_score
            + voice_score
        )
        total_score = max(0, min(100, total_score))  # Clamp score between 0 and 100

        return total_score
    except Exception as e:
        logging.error(f"Error calculating risk score: {e}")
        return 0
