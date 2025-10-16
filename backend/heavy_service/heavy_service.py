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

def run(n: int):
    result = _fibo(n) # First: Fibonacci
    return result
