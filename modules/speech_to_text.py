import json
import os
import wave
from pathlib import Path

from vosk import KaldiRecognizer, Model

BASE_MODEL_DIR = Path(__file__).resolve().parent.parent / "models"
MODEL_PATHS = {
    "en-us": BASE_MODEL_DIR / "vosk-model-small-en-us-0.15",
    "te": BASE_MODEL_DIR / "te" / "vosk-model-small-te-0.42",
    "en-in": BASE_MODEL_DIR / "en-in" / "vosk-model-en-in-0.5",
    "es": BASE_MODEL_DIR / "es" / "vosk-model-small-es-0.42",
    "fr": BASE_MODEL_DIR / "fr" / "vosk-model-small-fr-0.22",
    "hi": BASE_MODEL_DIR / "hi" / "vosk-model-small-hi-0.22",
}


def convert_speech_to_text(audio_file_path, language="en-us"):
    """Convert speech to text using Vosk models."""
    if language not in MODEL_PATHS:
        raise ValueError(f"Unsupported language: {language}")

    model_path = MODEL_PATHS[language]
    if not model_path.exists():
        raise ValueError(
            f"Vosk model for '{language}' not found at '{model_path}'. "
            "Please download it into the 'models/' folder."
        )

    if not os.path.exists(audio_file_path):
        raise ValueError(f"Audio file does not exist: {audio_file_path}")

    model = Model(str(model_path))

    try:
        wf = wave.open(audio_file_path, "rb")
    except wave.Error as exc:
        raise ValueError(f"Error opening audio file: {exc}") from exc

    if wf.getnchannels() != 1:
        wf.close()
        raise ValueError("Audio file must be mono PCM.")

    recognizer = KaldiRecognizer(model, wf.getframerate())
    transcript = ""

    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            transcript += result.get("text", "") + " "

    final_result = json.loads(recognizer.FinalResult())
    transcript += final_result.get("text", "")
    wf.close()

    return transcript.strip()
