from primesandfactors import is_prime
from math import log10
from collections import defaultdict

prime_cache = defaultdict(lambda: False)
def primetest(n):
    if n not in prime_cache:
        prime_cache[n] = is_prime(n)
    return prime_cache[n]

def c_prime(p1, p2):
    d1, d2 = int(log10(p1)) + 1, int(log10(p2)) + 1
    c2 = p2 * 10**d1 + p1
    c1 = p1 * 10**d2 + p2
    if primetest(c1) and primetest(c2):
        return True
    return False

def s_prime(arr1, arr2):
    for p1 in arr1:
        for p2 in arr2:
            if not c_prime(p1, p2):
                return False
    else:
        return True

def run(n=1000):
    primes = [n for n in range(3, n, 2) if primetest(n)]
    print(len(primes))

    pairs = set()
    for x in range(len(primes)):
        for y in range(x, len(primes)):
            p1, p2 = primes[x], primes[y]
            if c_prime(p1, p2):
                pairs.add((min(p1, p2), max(p1, p2)))
    print(len(pairs))

    threes = set()
    for p1 in pairs:
        for p2 in primes:
            if s_prime(p1, (p2,)):
                threes.add( tuple( sorted( p1 + (p2,) ) ) )
    print(len(threes))

    fours = set()
    for p1 in threes:
        for p2 in primes:
            if s_prime(p1, (p2,)):
                fours.add( tuple( sorted( p1 + (p2,) ) ) )
    print(fours)

    fives = set()
    for p1 in fours:
        for p2 in primes:
            if s_prime(p1, (p2,)):
                fives.add( tuple( sorted( p1 + (p2,) ) ) )
    print(fives)
    if not fives:
        run(n+1000)

def run2(n):
    primes = primes = [(n,) for n in range(3, n, 2) if primetest(n)]
    for p1 in primes:
        for p2 in primes:
            if s_prime(p1, p2):
                for p3 in primes:
                    if s_prime(p1+p2, p3):
                        for p4 in primes:
                            if s_prime(p1+p2+p3, p4):
                                print(p1, p2, p3, p4)
