import pytest

from modules.speech_to_text import convert_speech_to_text


def test_unsupported_language_raises_value_error():
    with pytest.raises(ValueError, match="Unsupported language"):
        convert_speech_to_text("audio/incoming_call1.wav", language="xx")


def test_missing_model_raises_value_error():
    with pytest.raises(ValueError, match="Vosk model"):
        convert_speech_to_text("audio/incoming_call1.wav", language="es")
