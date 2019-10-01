from functools import lru_cache

def fib(n):
    if n < 2:
        return n
    print(f'Calling fib({n - 2}) and fib({n -1})')
    return fib(n - 2) + fib(n - 1)

print('Calling fib', end='\n\n')
fib(10)

@lru_cache()
def fib_cached(n):
    if n < 2:
        return n
    print(f'Calling fib({n - 2}) and fib({n -1})')
    return fib_cached(n - 2) + fib_cached(n - 1)

print('Calling fib_cached', end='\n\n')
fib_cached(10)