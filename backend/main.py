from robyn import Robyn
from app.db.engine import Engine
from app.core.logger import logger
from app.api.routes.face import face_router

app = Robyn(__file__)


@app.startup_handler
async def startup_handler():
    logger.info("Starting up")
    logger.info("---Connecting to Postgres---")
    Engine()


@app.get("/")
async def entry(request):
    return "Hello, World"


app.include_router(face_router)
app.start(port=8080, host="0.0.0.0")
