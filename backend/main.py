import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from room import Room
from logger import init_logger

from race_service.race_service import get_existing_count
from leaky_service.leaky_service import get_active_count, get_active_players

from task import log_stats_task

# utils
init_logger()

api = FastAPI()
api.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

room = Room()


@api.on_event("startup")
async def start_background_tasks():
    asyncio.create_task(log_stats_task())


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
