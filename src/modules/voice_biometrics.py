# modules/voice_biometrics.py
from resemblyzer import VoiceEncoder, preprocess_wav
import numpy as np

# Initialize the voice encoder.
encoder = VoiceEncoder()


def get_voice_embedding(audio_file_path):
    """
    Extract a voice embedding from an audio file.

    :param audio_file_path: Path to the audio file.
    :return: A numpy array representing the voice embedding.
    """
    wav = preprocess_wav(audio_file_path)
    embedding = encoder.embed_utterance(wav)
    return embedding


def compare_voice_embeddings(embedding1, embedding2, threshold=0.8):
    """
    Compare two voice embeddings using cosine similarity.

    :param embedding1: First voice embedding.
    :param embedding2: Second voice embedding.
    :param threshold: Similarity threshold to consider a match.
    :return: True if embeddings match (similarity >= threshold), False otherwise.
    """
    cosine_similarity = np.dot(embedding1, embedding2) / (
        np.linalg.norm(embedding1) * np.linalg.norm(embedding2)
    )
    return cosine_similarity >= threshold


if __name__ == "__main__":
    embedding1 = get_voice_embedding("data/sample_audio/incoming_call.mp3")
    embedding2 = get_voice_embedding("data/sample_audio/bank_rep_sample.wav")
    match = compare_voice_embeddings(embedding1, embedding2)
    print("Voice match:", match)
