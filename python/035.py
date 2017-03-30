from primesandfactors import is_prime
from math import log

def rotate(n):
    l = int(log(n, 10)) + 1
    for _ in range(l):
        n *= 10
        n += n // 10**l
        n %= 10**l
        yield n

def circular_prime(n):
    for p in rotate(n):
        if not is_prime(p):
            return False
    return True

def all_odd(n):
    while n > 0:
        if n % 2 == 0: return False
        n //= 10
    return True

def circular_primes_below(n):
    print( sum([ circular_prime(n) for n in range(3, n) if all_odd(n) ]) + 1 ) #Add 1 to account for '2'
