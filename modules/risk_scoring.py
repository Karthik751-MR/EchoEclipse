from modules.nlp_analysis import detect_keywords, analyze_sentiment
from modules.caller_verification import is_trusted_number


def calculate_risk_score(
    transcript, language="en", metadata=None, caller_number=None, voice_match=False
):
    # Keyword score: each keyword adds 20 points
    keywords_found = detect_keywords(transcript, language)
    keyword_score = len(keywords_found) * 20

    # Sentiment: add 20 points if sentiment is negative
    sentiment = analyze_sentiment(transcript)
    sentiment_score = 20 if sentiment < 0 else 0

    # Metadata score: add 10 points for calls during odd hours (<6AM or >10PM)
    metadata_score = (
        10
        if metadata and (metadata.get("hour", 12) < 6 or metadata.get("hour", 12) > 22)
        else 0
    )

    # Caller adjustment: subtract 30 points if caller is trusted
    caller_score = -30 if caller_number and is_trusted_number(caller_number) else 0

    # Voice biometrics: subtract 20 points if voice matches trusted profile
    voice_score = -20 if voice_match else 0

    # Total risk score (clamped between 0 and 100)
    total_score = (
        keyword_score + sentiment_score + metadata_score + caller_score + voice_score
    )
    total_score = max(0, min(100, total_score))
    return total_score, keywords_found
