# NOTE: I calculated it for 2GB. Because I tried around 10MB and it crashed my WSL, lol. 
SIZE = 256 * 1024


class BigDto:
    def __init__(self):
        self.obj = bytearray(SIZE)
    def __del__(self):
        print(f"BigDto destroyed")
