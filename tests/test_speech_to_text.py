# tests/test_speech_to_text.py
import os
import unittest
from src.modules.speech_to_text import convert_speech_to_text


class TestSpeechToText(unittest.TestCase):
    def test_transcription(self):
        audio_path = "data/sample_audio/incoming_call.mp3"
        # Only run the test if the file exists.
        if os.path.exists(audio_path):
            transcript = convert_speech_to_text(audio_path, model_size="tiny")
            self.assertTrue(isinstance(transcript, str))
            self.assertTrue(len(transcript) > 0)
        else:
            self.skipTest(f"Audio file not found: {audio_path}")


if __name__ == "__main__":
    unittest.main()
