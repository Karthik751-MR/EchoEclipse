import os
import wave
import json
from vosk import Model, KaldiRecognizer


def convert_speech_to_text(audio_file_path, language="en-us"):
    """
    Convert speech to text using Vosk models.

    Args:
        audio_file_path (str): Path to the audio file.
        language (str): Language code (e.g., "en-us", "hi", "es", "fr", "te").

    Returns:
        str: Transcribed text.
    """
    # Map language codes to model directories
    model_paths = {
        "en-us": "models/en-us/vosk-model-small-en-us-0.15",
        "te": "models/te/vosk-model-small-te-0.42",
        "en-in": "models/en-in/vosk-model-en-in-0.5",
        "es": "models/es/vosk-model-small-es-0.42",
        "fr": "models/fr/vosk-model-small-fr-0.22",
        "hi": "models/hi/vosk-model-small-hi-0.22",
    }

    # Check if the specified language model exists
    if language not in model_paths:
        raise ValueError(f"Unsupported language: {language}")

    model_path = model_paths[language]
    if not os.path.exists(model_path):
        raise ValueError(
            f"Vosk model for '{language}' not found. Please download it into the 'models/' folder."
        )

    # Load the Vosk model
    model = Model(model_path)

    # Open the audio file
    try:
        wf = wave.open(audio_file_path, "rb")
    except wave.Error as e:
        raise ValueError(f"Error opening audio file: {e}")

    # Ensure the audio file is mono (Vosk requires mono PCM)
    if wf.getnchannels() != 1:
        raise ValueError("Audio file must be mono PCM.")

    # Initialize the recognizer
    recognizer = KaldiRecognizer(model, wf.getframerate())
    transcript = ""

    # Process the audio file in chunks
    while True:
        data = wf.readframes(4000)  # Read 4000 frames at a time
        if len(data) == 0:  # End of file
            break
        if recognizer.AcceptWaveform(data):  # Process the waveform
            result = json.loads(recognizer.Result())
            transcript += result.get("text", "") + " "

    # Process any remaining speech in the final chunk
    final_result = json.loads(recognizer.FinalResult())
    transcript += final_result.get("text", "")

    # Close the audio file
    wf.close()

    return transcript.strip()
