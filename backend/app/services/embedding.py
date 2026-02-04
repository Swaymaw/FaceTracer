import numpy as np


def generate_embedding(image_bytes: bytes) -> np.ndarray:
    rng = np.random.default_rng()
    return rng.random(512)
