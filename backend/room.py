import uuid
from logger import get_logger
from stats import log_stats
from heavy_service.heavy_service import HeavyService


logger = get_logger()


class Room:
    def __init__(self):
        self.players = {}
        self.service = HeavyService()

    async def join(self):
        await self.service.run(25)
        logger.info(f"Service [HeavyService] is complete.")

        id = str(uuid.uuid4())
        self.players[id] = id
        logger.info(f"Player {id} joined the room.")

        log_stats()
