from pydub import AudioSegment
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import numpy as np


def convert_mp3_to_wav(mp3_file, wav_file):
    """
    Convert an MP3 file to WAV format using pydub.
    """
    # Load the MP3 file
    audio = AudioSegment.from_mp3(mp3_file)
    # Export as WAV
    audio.export(wav_file, format="wav")


def extract_voice_features(audio_file):
    """
    Extract voice features from an audio file (supports MP3 and WAV).
    """
    # If the file is MP3, convert it to WAV
    if audio_file.endswith(".mp3"):
        wav_file = audio_file.replace(".mp3", ".wav")
        convert_mp3_to_wav(audio_file, wav_file)
        audio_file = wav_file

    try:
        # Read the WAV file
        [fs, x] = audioBasicIO.read_audio_file(audio_file)
    except Exception as e:
        raise ValueError(f"Error reading audio file {audio_file}: {e}")

    # Convert to mono if needed
    if len(x.shape) > 1:
        x = x[:, 0]

    # Define window and step sizes in seconds
    window_size = 1.0  # 1 second window
    step_size = 0.5  # 0.5 second step

    # Extract short-term features
    features, _ = ShortTermFeatures.feature_extraction(
        x, fs, window_size * fs, step_size * fs
    )
    return np.mean(features, axis=1)


def compare_voice_features(features1, features2, threshold=0.8):
    """
    Compare two voice feature vectors using cosine similarity.
    """
    # Normalize the feature vectors
    norm1 = np.linalg.norm(features1)
    norm2 = np.linalg.norm(features2)

    if norm1 == 0 or norm2 == 0:
        return 0.0  # Return similarity score 0.0 if either vector is zero

    cosine_similarity = np.dot(features1, features2) / (norm1 * norm2)
    return cosine_similarity >= threshold, cosine_similarity
