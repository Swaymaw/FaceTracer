from robyn import SubRouter
from robyn.robyn import Request

from app.services.embedding import generate_embedding
from app.services.vector_store import add_embedding

face_router = SubRouter(__file__, prefix="/face")


@face_router.post("/register")
async def register_face(request: Request):
    # print(request.files)
    if not request.files:
        return {"error": "No image uploaded", "status": 400}
    file_data = list(request.files.values())[0]
    file = bytearray(file_data)
    embedding = generate_embedding(file)
    add_embedding(embedding)
    return {"status": "registered"}
