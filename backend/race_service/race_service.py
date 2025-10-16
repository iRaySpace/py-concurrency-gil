import time
import threading

_existing_players = 0
_lock = threading.Lock()


def increment():
    global _existing_players
    time.sleep(0.05)
    _existing_players = _existing_players + 1


def increment_with_lock():
    global _existing_players
    time.sleep(0.05)
    with _lock:
        _existing_players = _existing_players + 1


def get_existing_players():
    return _existing_players
