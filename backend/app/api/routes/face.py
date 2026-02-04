from robyn import SubRouter
from robyn.robyn import Request
from uuid import uuid4

from app.services.embedding import generate_embedding
from app.services.vector_store import QdrantEngine

face_router = SubRouter(__file__, prefix="/face")


@face_router.post("/register")
async def register_face(request: Request):
    # print(request.files)
    qdrant = QdrantEngine()

    if not request.files:
        return {"error": "No image uploaded", "status": 400}

    file_data = list(request.files.values())[0]
    file = bytearray(file_data)

    id = str(uuid4())

    embedding = generate_embedding(file)
    qdrant.add_embedding(embedding, id=id)

    return {"status": "registered"}
