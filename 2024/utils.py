from time import time, perf_counter
from functools import wraps

def timing(func):
    @wraps(func)
    def wrap(*args, **kw):
        ts = perf_counter()
        result = func(*args, **kw)
        te = perf_counter()
        print(f'Timing: {func.__name__!r} executed in {(te-ts):.4f}s')
        return result
    return wrap



