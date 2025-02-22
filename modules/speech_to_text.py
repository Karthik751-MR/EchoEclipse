import os
import wave
import json
from vosk import Model, KaldiRecognizer


def convert_speech_to_text(audio_file_path):
    model_path = "models/vosk-model-small-en-us-0.15"
    if not os.path.exists(model_path):
        raise ValueError(
            "Vosk model not found. Please download it into the 'models/' folder."
        )

    model = Model(model_path)
    try:
        wf = wave.open(audio_file_path, "rb")
    except wave.Error as e:
        raise ValueError(f"Error opening audio file: {e}")

    if wf.getnchannels() != 1:
        raise ValueError("Audio file must be mono PCM.")

    recognizer = KaldiRecognizer(model, wf.getframerate())
    transcript = ""

    # Process in chunks and collect intermediate results
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            transcript += result.get("text", "") + " "
    # Process any remaining speech
    final_result = json.loads(recognizer.FinalResult())
    transcript += final_result.get("text", "")
    wf.close()
    return transcript.strip()
