# src/main.py
from modules.speech_to_text import convert_speech_to_text
from modules.language_detection import detect_language
from modules.risk_scoring import calculate_risk_score
from modules.alerting import send_email_alert


def process_call(audio_file_path, metadata, caller_number, recipient_email):
    # 1. Convert audio to text
    transcript = convert_speech_to_text(audio_file_path)
    print("Transcript:", transcript)

    # 2. Detect language from the transcript
    language = detect_language(transcript)
    print("Detected Language:", language)

    # 3. Calculate risk score (voice biometrics set to False for now)
    risk_score, keywords = calculate_risk_score(
        transcript, language, metadata, caller_number, voice_match=False
    )
    print("Risk Score:", risk_score)

    # 4. If risk score is high, send an email alert
    if risk_score >= 60:
        subject = "Scam Alert!"
        message = (
            f"Risk Score: {risk_score}\nKeywords: {keywords}\nTranscript: {transcript}"
        )
        send_email_alert(subject, message, recipient_email)
        return {"status": "alert_sent", "risk_score": risk_score}
    else:
        return {"status": "safe", "risk_score": risk_score}


if __name__ == "__main__":
    # Example metadata: call received at 11 PM
    call_metadata = {"hour": 23}
    # Replace with actual values as needed.
    result = process_call(
        "data/sample_audio/incoming_call.mp3",
        call_metadata,
        "+18001234567",
        "recipient@example.com",
    )
    print("Processing Result:", result)
