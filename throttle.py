# throttle.py
import time
from functools import wraps

REQUESTS_PER_MINUTE = 250
INTERVAL = 60 / REQUESTS_PER_MINUTE
_last_call = {}

def rate_limit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        now = time.time()
        func_name = func.__name__
        elapsed = now - _last_call.get(func_name, 0)
        if elapsed < INTERVAL:
            time.sleep(INTERVAL - elapsed)
        _last_call[func_name] = time.time()
        return func(*args, **kwargs)
    return wrapper
