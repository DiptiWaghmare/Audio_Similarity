import os
import torch
import numpy as np
from pyannote.audio import Inference
from huggingface_hub import login
from sklearn.metrics.pairwise import cosine_similarity

# Login using Streamlit secret
login(token=os.getenv("HF_TOKEN"))

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
inference = Inference("pyannote/embedding", device=device)

def extract_embedding(file_path):
    return inference(file_path).data.mean(axis=0).reshape(1, -1)

def get_similarity_score(embedding1, embedding2):
    return float(cosine_similarity(embedding1, embedding2)[0][0])





