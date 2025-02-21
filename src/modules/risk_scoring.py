# modules/risk_scoring.py
from modules.nlp_analysis import detect_keywords, analyze_sentiment
from modules.caller_verification import is_trusted_number


def calculate_risk_score(
    transcript, language="en", metadata=None, caller_number=None, voice_match=False
):
    """
    Calculate a risk score based on various factors.

    :param transcript: The transcribed text from the call.
    :param language: Detected language of the transcript.
    :param metadata: Additional metadata (e.g., call hour).
    :param caller_number: The caller's phone number.
    :param voice_match: Boolean indicating if voice biometrics matched.
    :return: A tuple containing the risk score (0-100) and the detected keywords.
    """
    # Keyword score: each found keyword adds 20 points.
    keywords_found = detect_keywords(transcript, language)
    keyword_score = len(keywords_found) * 20

    # Sentiment score: add 20 points if sentiment is negative.
    sentiment = analyze_sentiment(transcript)
    sentiment_score = 20 if sentiment and sentiment[0]["label"] == "NEGATIVE" else 0

    # Metadata score: add 10 points if call is received at odd hours (before 6am or after 10pm).
    metadata_score = 0
    if metadata and (metadata.get("hour", 12) < 6 or metadata.get("hour", 12) > 22):
        metadata_score = 10

    # Caller verification: reduce risk by 30 if caller is trusted.
    caller_score = -30 if caller_number and is_trusted_number(caller_number) else 0

    # Voice biometrics: reduce risk by 20 if voice matches the known profile.
    voice_score = -20 if voice_match else 0

    total_score = max(
        min(
            keyword_score
            + sentiment_score
            + metadata_score
            + caller_score
            + voice_score,
            100,
        ),
        0,
    )
    return total_score, keywords_found


if __name__ == "__main__":
    metadata_example = {"hour": 23}
    score, keywords = calculate_risk_score(
        "Your bank requires urgent confirmation of your account number.",
        language="en",
        metadata=metadata_example,
        caller_number="+18001234567",
        voice_match=False,
    )
    print("Risk Score:", score)
    print("Detected Keywords:", keywords)
