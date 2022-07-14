from time import sleep
from functools import lru_cache


def tick(*args, **kwargs):
    print(*args, end='', flush=False, **kwargs)


def fib_naive(n):
    """Recursive fib with naive approach."""

    if n < 2:
        return n

    tick(f'|')
    return fib_naive(n - 2) + fib_naive(n - 1)


cache = {}
def fib_cache(n):
    """Recursive fib with cache to fix multiple repetitive calls."""

    if n < 2:
        return n
    if n in cache.keys():
        return cache[n]

    tick(f'|')
    res = fib_cache(n - 2) + fib_cache(n - 1)
    cache[n] = res

    return res


@lru_cache()
def fib_lru_cache(n):
    """Recursive fib using python functools.lru_cache to fix multiple repetitive calls."""

    if n < 2:
        return n

    tick(f'|')
    return fib_lru_cache(n - 2) + fib_lru_cache(n - 1)


if __name__ == '__main__':
    N = 10

    print('Calling fib')
    print(f'result: {fib_naive(N)}')

    print('Calling fib_cache')
    print(f'result: {fib_cache(N)}')

    print('Calling fib_lru_cache')
    print(f'result: {fib_lru_cache(N)}')
