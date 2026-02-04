import faiss

import numpy as np
from app.core.config import settings

index = faiss.IndexFlatL2(settings.embedding_dim)


def add_embedding(vec: np.ndarray):
    index.add(vec.reshape(1, -1))


def search(vec: np.ndarray, k: int = 5):
    return index.search(vec.reshape(1, -1), k)
