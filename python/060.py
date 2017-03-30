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

def run():
    primes = primes = [(n,) for n in range(3, 9000, 2) if primetest(n)]
    for p1 in primes:
        for p2 in primes:
            if s_prime(p1, p2):
                for p3 in primes:
                    if s_prime(p1+p2, p3):
                        for p4 in primes:
                            if s_prime(p1+p2+p3, p4):
                                print(p1[0], p2[0], p3[0], p4[0])
                                for p5 in primes:
                                    if s_prime(p1+p2+p3+p4, p5):
                                        return p1+p2+p3+p4+p5
