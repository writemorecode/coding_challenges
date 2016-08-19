# Project Euler - Problem 2
# Calculate the sum of all even fibonacci numbers that do not exceed 4 million.
# Uses lru_cache from functools for memoization (speed)

import functools

@functools.lru_cache(None)
def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)

def sum_fibs():
    fibsum = 0
    i = 0
    while True:
        f = fib(i)
        i += 1
        if f % 2 == 0:
            if f < 4000000:
                fibsum += f
            else:
                return fibsum

if __name__ == '__main__':
    answer = sum_fibs()
    print(answer)
    assert answer == 4613732
