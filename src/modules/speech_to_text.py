# modules/speech_to_text.py
import whisper


def convert_speech_to_text(audio_file_path, model_size="base"):
    """
    Transcribe an audio file using OpenAI's Whisper model.

    :param audio_file_path: Path to the audio file.
    :param model_size: Model size to use (e.g., "tiny", "base", "small", "medium", "large").
    :return: The transcribed text.
    """
    model = whisper.load_model(model_size)
    result = model.transcribe(audio_file_path)
    return result["text"]


if __name__ == "__main__":
    transcript = convert_speech_to_text("data/sample_audio/incoming_call.mp3")
    print("Transcript:", transcript)
