from math import sqrt
from collections import Counter
from itertools import permutations
from time import time

cache = {}
seen = {}

def is_prime(n):
    if n == 2: return True
    if n < 2 or not n % 2: return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def primes(lo, hi):
    i = lo
    while i < hi:
        if is_prime(i): yield i
        i += 1 + (i % 2)

def to_int(tup):
    # return tup[0] * 1000 + tup[1] * 100 + tup[2] * 10 + tup[3]
    return int(''.join(map(str, tup)))
def prime_permutations(num):
    arr = []
    while num > 0:
        arr.append(num % 10)
        num //= 10
    for p in permutations(arr):
        n = to_int(p)
        if cache.get(n) and not seen.get(n):
            seen[n] = True
            yield n

def cache_primes(n1, n2):
    for p in primes(n1, n2):
        cache[p] = True

def run(n1, n2):
    for n in range(n1, n2):
        if cache.get(n) and not seen.get(n):
            a = [ p for p in prime_permutations(n) ]
            if(len(a)) > 2:
                for n1 in a:
                    diffs = {}
                    for n2 in a:
                        diff = abs(n1 - n2)
                        count = diffs.get(diff) or 0
                        diffs[diff] = count + 1
                        if count > 0:
                            process = lambda x: abs(x - n2) in [diff, 2*diff, 0, 3*diff]
                            b = sorted(list(filter(process, a)))
                            # print(b[0]*10**8 + b[1]*10**4 + b[2])

t0 = time()
for _ in range(100):
    cache_primes(1000, 10000)
    run(1000, 10000)
t1 = time()
print((t1 - t0) / 100)
