from dataclasses import dataclass


@dataclass
class Settings:
    database_url = "postgresql://postgres:facetrace@localhost:5432/facetrace"
    qdrant_url = "http://localhost:6333"
    embedding_dim: int = 512
    embedding_collection = "face_embeddings"


settings = Settings()
