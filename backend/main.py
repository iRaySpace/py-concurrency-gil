from fastapi import FastAPI
from room import Room
from logger import init_logger

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
    return {"total_players": len(room.players)}
