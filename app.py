from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

from core.config import settings
from routes import index, cars, search

app = FastAPI(
    title=settings.SERVICE_NAME,
    default_response_class=ORJSONResponse,
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")


# routes
app.include_router(
    index.router,
    tags=["index"]
)
app.include_router(
    cars.router,
    tags=["cars"]
)
app.include_router(
    search.router,
    tags=["search"]
)
