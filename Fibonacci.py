from functools import lru_cache
import time

# Recursive Fibonacci with Memoization
@lru_cache(maxsize=None)
def fibonacci_recursive(n: int) -> int:
    """Recursive Fibonacci using memoization (cache)."""
    if n < 0:
        raise ValueError("Fibonacci number cannot be negative")
    elif n in [0, 1]:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative Fibonacci
def fibonacci_iterative(n: int) -> int:
    """Iterative Fibonacci approach (efficient for large n)."""
    if n < 0:
        raise ValueError("Fibonacci number cannot be negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Fibonacci Generator (for large sequences)
def fibonacci_generator():
    """Generator function to yield Fibonacci numbers infinitely."""
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Performance Testing
n = 30

start_time = time.time()
print(f"Recursive: {fibonacci_recursive(n)}")
print(f"Time taken: {time.time() - start_time:.6f} sec")

start_time = time.time()
print(f"Iterative: {fibonacci_iterative(n)}")
print(f"Time taken: {time.time() - start_time:.6f} sec")

# Generating first 10 Fibonacci numbers using generator
fib_gen = fibonacci_generator()
print("First 10 Fibonacci numbers using generator:", [next(fib_gen) for _ in range(10)])
