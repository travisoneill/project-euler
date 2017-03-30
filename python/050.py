from collections import deque
from time import time
# Lower bound on length is 21 from example.  Therefore highest possible average
# of sequence is 50000.

cache = { 2: True }
def is_prime(n):
    if cache.get(n): return True
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1 + i%2
    cache[n] = True
    return True

def prime_gen():
    '''WARNING: infinite loop. must break manually'''
    yield 2
    n = 3
    while True:
        if is_prime(n):
            yield n
        n += 2

def find_max(n):
    '''return max possible range of conscutive primes that sums to less than n'''
    s = 0
    i = 0
    for p in prime_gen():
        s += p
        i += 1
        if s > n:
            return i

def p_range(window, limit):
    '''returns first prime < limit that can be made by the sum of n consecutive primes'''
    primes = deque()
    count = 0
    for i, n in enumerate(prime_gen()):
        count += n
        primes.append(n)
        if len(primes) > window:
            count -= primes.popleft()
        if count > limit:
            break
        if len(primes) == window and is_prime(count):
            print(window)
            return count

def search(limit):
    max_possible = find_max(limit)
    for n in reversed(range(max_possible)):
        x = p_range(n, limit)
        if x: return x

def run():
    search(1000000)

#BENCHMARK
def bm(n):
    t0 = time()
    search(n)
    t1 = time()
    print(t1-t0)
