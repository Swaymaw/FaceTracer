from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct
from app.core.config import settings
import numpy as np


class QdrantEngine:
    instance = None

    def __init__(self):
        self.client = QdrantClient(url=settings.qdrant_url)
        self.init_collection()

    def init_collection(self):
        if not self.client.collection_exists(settings.embedding_collection):
            self.client.create_collection(
                collection_name=settings.embedding_collection,
                vectors_config=VectorParams(
                    size=settings.embedding_dim, distance=Distance.COSINE
                ),
            )

    def add_embedding(self, vec: np.ndarray, id: str):
        self.client.upsert(
            collection_name=settings.embedding_collection,
            points=[PointStruct(id=id, vector=vec.tolist())],
        )

    def search(self, vec: np.ndarray, k: int = 5):
        results = self.client.search(
            collection_name=settings.embedding_collection,
            query_vector=vec.tolist(),
            limit=k,
        )
        return results

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance
