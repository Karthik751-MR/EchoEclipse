import csv
from datetime import datetime
from modules.speech_to_text import convert_speech_to_text
from modules.language_detection import detect_language
from modules.nlp_analysis import detect_keywords, analyze_sentiment
from modules.caller_verification import is_trusted_number
from modules.voice_biometrics import compare_voice_features, extract_voice_features
from modules.risk_scoring import calculate_risk_score
from modules.alerting import alert_user

# CSV file to log call details
CALL_LOG_FILE = "call_logs.csv"


def log_call_details(call_details):
    """
    Log call details to a CSV file.
    """
    # Define the CSV header if the file doesn't exist
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

    # Write to CSV
    with open(CALL_LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=header)
        # Write header if the file is empty
        if file.tell() == 0:
            writer.writeheader()
        writer.writerow(call_details)


def process_call(audio_file_path, metadata, caller_number, user_contact):
    """
    Process an incoming call and determine if it's a potential scam.
    """
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
        # 1. Convert speech to text
        transcript = convert_speech_to_text(audio_file_path)
        call_details["transcript"] = transcript
        print("Transcript:", transcript)

        # 2. Detect language
        language = detect_language(transcript)
        call_details["language"] = language
        print("Language Detected:", language)

        # 3. Verify caller ID
        trusted = is_trusted_number(caller_number)
        call_details["trusted_caller"] = trusted
        if trusted:
            print(f"Caller is trusted: {trusted}")

        # 4. (Optional) Voice biometrics – uncomment if you have a known voice sample
        voice_match = False
        # known_features = extract_voice_features("audio/known_voice.wav")
        # call_features = extract_voice_features(audio_file_path)
        # voice_match = compare_voice_features(known_features, call_features)
        call_details["voice_match"] = voice_match

        # 5. Calculate risk score
        risk_score, keywords = calculate_risk_score(
            transcript, language, metadata, caller_number, voice_match
        )
        call_details["risk_score"] = risk_score
        call_details["keywords"] = keywords
        print("Risk Score:", risk_score)
        print("Keywords Detected:", keywords)

        # 6. Alert user if risk score is high (score ≥ 60)
        if risk_score >= 60:
            alert_user(risk_score, keywords, user_contact)
            call_details["status"] = "alert_sent"
            print("Alert sent to user.")
        else:
            print("Call is safe.")

    except Exception as e:
        print(f"Error processing call: {e}")
        call_details["status"] = f"error: {str(e)}"

    # Log call details to CSV
    log_call_details(call_details)
    return call_details


if __name__ == "__main__":
    # Example call metadata (e.g., call received at 11 PM)
    call_metadata = {"hour": 23}

    # User contact details: email and WhatsApp phone number (formatted with country code)
    user_contact = {"email": "aajeethan7@gmail.com", "whatsapp": "+919791006878"}

    # Caller number to verify (example number)
    caller_number = "+18001234567"

    # List of WAV files to process (assuming files are in an 'audio/' subdirectory)
    audio_files = [
        "audio/incoming_call1.wav",
        "audio/incoming_call2.wav",
        "audio/incoming_call3.wav",
        "audio/incoming_call4.wav",
        "audio/incoming_call5.wav",
    ]

    # Process each call
    for audio_file in audio_files:
        print(f"\nProcessing file: {audio_file}")
        result = process_call(audio_file, call_metadata, caller_number, user_contact)
        print("Processing Result:", result)
        print("-" * 40)  # Separator for readability
