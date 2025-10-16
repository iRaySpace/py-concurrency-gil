from fastapi import FastAPI
from room import Room
from logger import init_logger
from race_service.race_service import get_existing_players

init_logger()

api = FastAPI()
room = Room()


@api.get("/ping")
def get_ping():
    return {"message": "pong"}


@api.post("/join")
async def post_join():
    await room.join()
    return {"status": "ok"}


@api.get("/info")
def get_info():
    return {
        "active_players": len(room.active_players),
        "existing_players": get_existing_players(),
    }
