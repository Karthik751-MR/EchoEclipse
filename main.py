import csv
from datetime import datetime

from modules.alerting import alert_user
from modules.caller_verification import is_trusted_number
from modules.language_detection import detect_language
from modules.risk_scoring import calculate_risk_score
from modules.speech_to_text import convert_speech_to_text

CALL_LOG_FILE = "call_logs.csv"


def log_call_details(call_details):
    """Append call details to CSV log file."""
    header = [
        "timestamp",
        "caller_number",
        "audio_file",
        "transcript",
        "language",
        "trusted_caller",
        "voice_match",
        "risk_score",
        "keywords",
        "status",
    ]

    with open(CALL_LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(call_details)


def process_call(audio_file_path, metadata, caller_number, user_contact):
    """Process an incoming call and determine whether it is suspicious."""
    call_details = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "caller_number": caller_number,
        "audio_file": audio_file_path,
        "transcript": "",
        "language": "",
        "trusted_caller": False,
        "voice_match": False,
        "risk_score": 0,
        "keywords": [],
        "status": "safe",
    }

    try:
        transcript = convert_speech_to_text(audio_file_path)
        call_details["transcript"] = transcript

        language = detect_language(transcript)
        call_details["language"] = language

        trusted = is_trusted_number(caller_number)
        call_details["trusted_caller"] = trusted

        voice_match = False
        call_details["voice_match"] = voice_match

        risk_score, keywords = calculate_risk_score(
            transcript=transcript,
            language=language,
            metadata=metadata,
            caller_number=caller_number,
            voice_match=voice_match,
        )
        call_details["risk_score"] = risk_score
        call_details["keywords"] = keywords

        if risk_score >= 60:
            alert_user(risk_score, keywords, user_contact)
            call_details["status"] = "alert_sent"
        else:
            call_details["status"] = "safe"

    except Exception as exc:
        call_details["status"] = f"error: {exc}"

    log_call_details(call_details)
    return call_details


if __name__ == "__main__":
    call_metadata = {"hour": 23}
    user_contact = {
        "email": "user@example.com",
        "whatsapp": "+10000000000",
        "phone": "+10000000000",
    }
    caller_number = "+18001234567"

    audio_files = [
        "audio/incoming_call1.wav",
        "audio/incoming_call2.wav",
        "audio/incoming_call3.wav",
    ]

    for audio_file in audio_files:
        print(f"\nProcessing file: {audio_file}")
        result = process_call(audio_file, call_metadata, caller_number, user_contact)
        print("Processing Result:", result)
        print("-" * 40)
