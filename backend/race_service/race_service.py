import time
import threading

_existing_players = 0
_lock = threading.Lock()


def increment():
    global _existing_players
    temp = _existing_players
    time.sleep(0.001)
    _existing_players = temp + 1


def increment_with_lock():
    with _lock:
        increment()


def get_existing_players():
    return _existing_players
