import tracemalloc
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from room import Room
from logger import init_logger
from stats import log_mem_diff, log_stats

from race_service.race_service import get_existing_count
from leaky_service.leaky_service import get_active_count, get_active_players

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

@api.get("/ping")
def get_ping():
    return {"message": "pong"}


@api.post("/play")
async def post_play():
    # NOTE: We snapshot for the memory usage
    before = tracemalloc.take_snapshot()

    # Where the processing begins!
    await room.play()

    # NOTE: Snapshot also after
    after = tracemalloc.take_snapshot()

    log_mem_diff(before, after)
    log_stats()

    return {"status": "ok"}


@api.get("/info")
def get_info():
    return {
        "existing_count": get_existing_count(),
        "active_count": get_active_count(),
        "active_players": get_active_players(),
    }
