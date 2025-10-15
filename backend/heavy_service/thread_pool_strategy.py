import asyncio
import multiprocessing
from concurrent.futures import ThreadPoolExecutor
from heavy_service.pool_strategy import PoolStrategy
from logger import get_logger

logger = get_logger()


class ThreadPoolStrategy(PoolStrategy):
    def __init__(self):
        self.pool_executor = ThreadPoolExecutor(max_workers=multiprocessing.cpu_count())

    async def run(self, func, *args, **kwargs):
        logger.info("Running function in [ThreadPoolDecorator]")
        return asyncio.get_event_loop().run_in_executor(self.pool_executor, func, *args, **kwargs)
