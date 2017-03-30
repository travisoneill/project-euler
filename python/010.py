from math import sqrt
from time import time

# ONE LINER (extremely slow)
print(sum([x for x in range(2, 2000000) if not [y for y in range(2, int(sqrt(x))+1) if x % y == 0]]))

prime_cache = []
def is_prime_dynamic(n):
    if n == 2: return True
    if n < 2 or not n % 2: return False
    for p in prime_cache:
        if p > sqrt(n): break
        if n % p == 0: return False
    prime_cache.append(n)
    return True

def primes_dynamic(n):
    i = 2
    while i < n:
        if is_prime_dynamic(i): yield i
        i += 1 + (i % 2)

# RUN
print(primes_dynamic(2000000))

def is_prime(n):
    if n == 2: return True
    if n < 2 or not n % 2: return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes(n):
    i = 2
    while i < n:
        if is_prime(i): yield i
        i += 1 + (i % 2)

#BENCHMARK
# def test1():
#     sum(primes(2000000))
#
# def test2():
#     sum(primes_dynamic(2000000))
#
# def bm(f, n):
#     t0 = time()
#     for _ in range(n):
#         f()
#     t1 = time()
#     print(t1-t0)
#
# bm(test1, 1)
# bm(test2, 1)
