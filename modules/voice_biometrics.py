from pydub import AudioSegment
from pyAudioAnalysis import audioBasicIO
from pyAudioAnalysis import ShortTermFeatures
import numpy as np
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def convert_mp3_to_wav(mp3_file, wav_file):
    """
    Convert an MP3 file to WAV format using pydub.

    Args:
        mp3_file (str): Path to the input MP3 file.
        wav_file (str): Path to save the output WAV file.
    """
    try:
        # Load the MP3 file
        audio = AudioSegment.from_mp3(mp3_file)
        # Export as WAV
        audio.export(wav_file, format="wav")
        logging.info(f"Converted {mp3_file} to {wav_file}")
    except Exception as e:
        logging.error(f"Error converting MP3 to WAV: {e}")
        raise


def extract_voice_features(audio_file):
    """
    Extract voice features from an audio file (supports MP3 and WAV).

    Args:
        audio_file (str): Path to the audio file.

    Returns:
        np.ndarray: Mean of short-term features extracted from the audio.
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
        logging.error(f"Error reading audio file {audio_file}: {e}")
        raise ValueError(f"Error reading audio file {audio_file}: {e}")

    # Convert to mono if needed
    if len(x.shape) > 1:
        x = x[:, 0]

    # Define window and step sizes in seconds
    window_size = 1.0  # 1 second window
    step_size = 0.5  # 0.5 second step

    # Extract short-term features
    try:
        features, _ = ShortTermFeatures.feature_extraction(
            x, fs, window_size * fs, step_size * fs
        )
        return np.mean(features, axis=1)
    except Exception as e:
        logging.error(f"Error extracting features from {audio_file}: {e}")
        raise ValueError(f"Error extracting features from {audio_file}: {e}")


def compare_voice_features(features1, features2, threshold=0.8):
    """
    Compare two voice feature vectors using cosine similarity.

    Args:
        features1 (np.ndarray): Feature vector of the first audio.
        features2 (np.ndarray): Feature vector of the second audio.
        threshold (float): Similarity threshold (default: 0.8).

    Returns:
        tuple: A tuple containing a boolean (True if similar, False otherwise) and the cosine similarity score.
    """
    try:
        # Normalize the feature vectors
        norm1 = np.linalg.norm(features1)
        norm2 = np.linalg.norm(features2)

        if norm1 == 0 or norm2 == 0:
            return False, 0.0  # Return similarity score 0.0 if either vector is zero

        cosine_similarity = np.dot(features1, features2) / (norm1 * norm2)
        return cosine_similarity >= threshold, cosine_similarity
    except Exception as e:
        logging.error(f"Error comparing voice features: {e}")
        raise ValueError(f"Error comparing voice features: {e}")
