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
        await websocket.send_json({
            "data": {
                "provider": "https://test.com",
                "url": "https://turbo.kg/cars/ZxJgMH2E",
                "price": 7000,
                "image": "https://turbo.kg/images/005/410/163/b01e38c3a9d0f6b023ce38a843f248d2-standard2x.jpg",
            }
        })


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
