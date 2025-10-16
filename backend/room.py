import uuid
from logger import get_logger

from pool_strategy.thread_pool_strategy import ThreadPoolStrategy
from pool_strategy.process_pool_strategy import ProcessPoolStrategy

from leaky_service import leaky_service
from heavy_service import heavy_service
from race_service import race_service

from big_dto.big_dto import BigDto


logger = get_logger()
RUNS = 40


class Room:
    def __init__(self):
        self.strategy = ThreadPoolStrategy()

    async def play(self):
        # First: Memory Leak
        id = str(uuid.uuid4())
        player = BigDto(id)
        await self.strategy.run(leaky_service.add_player, player)
        logger.info(f"Player {id} joined the room.")

        # Second: GIL Limitations
        await self.strategy.run(heavy_service.run, RUNS, player)
        logger.info(f"Service [HeavyService] is complete.")

        # Third: Race Conditions
        await self.strategy.run(race_service.increment, player)
