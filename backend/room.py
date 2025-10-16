import uuid
from logger import get_logger
from stats import log_stats
from heavy_service import heavy_service
from race_service import race_service
from pool_strategy.thread_pool_strategy import ThreadPoolStrategy
from pool_strategy.process_pool_strategy import ProcessPoolStrategy
from big_dto.big_dto import BigDto


logger = get_logger()
RUNS = 40


class Room:
    def __init__(self):
        self.active_players = {}
        self.strategy = ThreadPoolStrategy()

    async def join(self):
        # First: Memory Leak
        id = str(uuid.uuid4())
        self.active_players[id] = BigDto()
        logger.info(f"Player {id} joined the room.")

        # Second: GIL Limitations
        await self.strategy.run(heavy_service.run, RUNS)
        logger.info(f"Service [HeavyService] is complete.")

        # Third: Race Conditions
        await self.strategy.run(race_service.increment)

        # Log Stats
        log_stats()
