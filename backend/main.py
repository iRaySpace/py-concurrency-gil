from fastapi import FastAPI
from room import Room
from logger import init_logger
from race_service.race_service import get_existing_count
from leaky_service.leaky_service import get_active_count, get_active_players

init_logger()

api = FastAPI()
room = Room()


@api.get("/ping")
def get_ping():
    return {"message": "pong"}


@api.post("/play")
async def post_play():
    await room.play()
    return {"status": "ok"}


@api.get("/info")
def get_info():
    return {
        "existing_count": get_existing_count(),
        "active_count": get_active_count(),
        "active_players": get_active_players(),
    }
