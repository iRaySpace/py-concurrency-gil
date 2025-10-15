from heavy_service.process_pool_strategy import ProcessPoolStrategy
from heavy_service.thread_pool_strategy import ThreadPoolStrategy


class HeavyService:
    def __init__(self):
        self.strategy = ProcessPoolStrategy()

    async def run(self, n: int):
        return await self.strategy.run(_heavy_run, n)


# NOTE: Just a simple fibonacci to simulate CPU-bound tasks
# This is implemented as top because Process Pool needs picklable
_cache = {}
def _heavy_run(n: int):
    if n in _cache:
        return _cache.get(n)
    if n <= 1:
        result = n
    else:
        result = _heavy_run(n - 1) + _heavy_run(n - 2)
    _cache[n] = result
    return result
