from big_dto.big_dto import BigDto
from logger import get_logger

logger = get_logger()


# NOTE: Just a simple fibonacci to simulate CPU-bound tasks
# This is implemented as top because Process Pool needs picklable
_cache = {}

def _fibo(n: int):
    if n in _cache:
        return _cache.get(n)
    if n <= 1:
        result = n
    else:
        result = _fibo(n - 1) + _fibo(n - 2)
    _cache[n] = result
    return result

def run(n: int, player: BigDto):
    result = _fibo(n) # First: Fibonacci
    logger.info(f"Player {player.id} is finished playing.")
    return result
