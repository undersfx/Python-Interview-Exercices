print('Normal Function')
def square(n):
    """Return the the square of N"""
    return n * n

print(square(3))
help(square)

def floatify(f):
    def inner(n):
        result = f(n)
        return float(result)
    return inner

print('Simple Decorator')
@floatify
def square(n):
    """Return the the square of N"""
    return n * n

print(square(3))
help(square)

print('Wraping Metadata')
from functools import wraps

def floatify(f):
    @wraps(f) # The magic happens here
    def inner(n):
        result = f(n)
        return float(result)
    return inner

@floatify
def square(n):
    """Return the the square of N"""
    return n * n

print(square(3))
help(square)
