from app.db.base import Base
from sqlalchemy import Column, Integer, ForeignKey, String


class FaceEmbedding(Base):
    __tablename__ = "face_embedding"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    embedding_hash = Column(String)
