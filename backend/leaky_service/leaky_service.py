import weakref
from big_dto.big_dto import BigDto


# NOTE: Using in-memory to demonstrate memory leak.
_active_players = {}

# FIX: Use WeakValueDictionary
# _active_players = weakref.WeakValueDictionary()


def add_player(player: BigDto):
    _active_players[player.id] = player


def get_active_count():
    return len(_active_players)


def get_active_players():
    return list(_active_players.keys())
