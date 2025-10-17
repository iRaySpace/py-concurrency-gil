import time
import threading
import multiprocessing
from logger import get_logger
from big_dto.big_dto import BigDto


logger = get_logger()

# NOTE: Thread Pool
_existing_count = 0
_lock = threading.Lock()

# NOTE: Process Pool
# _existing_count = multiprocessing.Value('i', 0)
# _lock = multiprocessing.Lock()


def increment(player: BigDto):
    global _existing_count
    temp = _existing_count
    # temp = _existing_count.value
    time.sleep(0.005)
    _existing_count = temp + 1
    # _existing_count.value = temp + 1
    logger.info(f"Player {player.id} is added to existing players.")


def increment_with_lock(player: BigDto):
    with _lock:
        increment(player)


def get_existing_count():
    # NOTE: Process Pool
    # return _existing_count.value
    return _existing_count
