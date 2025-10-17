import asyncio
import tracemalloc
from logger import get_logger
from stats import log_stats, log_mem_diff

logger = get_logger()
LOG_INTERVAL_SECS = 10

async def log_stats_task():
    tracemalloc.start()
    logger.info("Starting log_stats_task.")

    before = tracemalloc.take_snapshot()
    while True:
        await asyncio.sleep(LOG_INTERVAL_SECS)

        after = tracemalloc.take_snapshot()
        log_mem_diff(before, after)
        log_stats()

        before = after # Cycle snapshot
