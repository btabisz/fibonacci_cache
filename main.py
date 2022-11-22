import time
from functools import lru_cache


def fibonacci(n):
    if n <= 2:
        result = n
    else:
        result = fibonacci(n-1) + fibonacci(n-2)

    return result


@lru_cache(maxsize=100)
def fibonacci_cache(n):
    if n <= 2:
        result = n
    else:
        result = fibonacci_cache(n-1) + fibonacci_cache(n-2)

    return result


a = 35

time_start = time.time()
print(fibonacci(a))
time_stop = time.time()
print(time_stop-time_start)


time_start1 = time.time()
print(fibonacci_cache(a))
time_stop1 = time.time()
print(time_stop1 - time_start1)
print(fibonacci_cache.cache_info())

