import librosa
import torch
import numpy as np
from pyannote.audio import Inference
from sklearn.metrics.pairwise import cosine_similarity

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load pyannote speaker embedding model
inference = Inference("pyannote/embedding", device=device)

# Extract average embedding for audio file
def extract_embedding(file_path):
    return inference(file_path).data.mean(axis=0).reshape(1, -1)

# Compute cosine similarity between two embeddings
def get_similarity_score(embedding1, embedding2):
    return float(cosine_similarity(embedding1, embedding2)[0][0])
