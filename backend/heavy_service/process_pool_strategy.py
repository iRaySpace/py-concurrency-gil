import asyncio
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from heavy_service.pool_strategy import PoolStrategy
from logger import get_logger

logger = get_logger()


class ProcessPoolStrategy(PoolStrategy):
    def __init__(self):
        self.pool_executor = ProcessPoolExecutor(max_workers=multiprocessing.cpu_count())

    async def run(self, func, *args, **kwargs):
        logger.info("Running function in [ProcessPoolStrategy]")
        return asyncio.get_event_loop().run_in_executor(self.pool_executor, func, *args, **kwargs)
