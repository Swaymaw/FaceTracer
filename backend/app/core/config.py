from dataclasses import dataclass


@dataclass
class Settings:
    database_url = "postgresql://postgres:facetrace@localhost:5432/facetrace"
    embedding_dim: int = 512


settings = Settings()
