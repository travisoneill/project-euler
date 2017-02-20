from primesandfactors import is_prime
from math import sqrt

def triangular(limit):
    '''Generates triangular numbers up to limit.  Pass 'None' as argument to infinite loop'''
    if not limit: print('WARNING: Running in infinite loop mode')
    tri = lambda n: (n**2 + n) // 2
    i = 1
    while not limit or i < limit + 1:
        yield tri(i)
        i += 1

def primes(limit):
    '''Generates prime numbers up to limit.  Pass 'None' as argument to infinite loop'''
    if not limit: print('WARNING: Running in infinite loop mode')
    yield 2
    i = 3
    while not limit or i < limit:
        if is_prime(i):
            yield i
        i += 2


def primes2(limit):
    '''Generates prime numbers up to limit.  Pass 'None' as argument to infinite loop'''
    if limit < 4:
        sieve = [2, 3]
    else:
        sieve = [ n for n in primes2( int(sqrt(limit)) ) ]
    # print(sieve)
    for prime in sieve: yield prime
    i = sieve[-1] + 2
    while i <= limit:
        # print(i, limit)
        for prime in sieve:
            if not i % prime: break
            if prime * prime > i:
                yield i
                break
        else:
            yield i
        i += 2

def get_test_list(n):
    if n < 2047: return [2]
    if n < 1373653: return [2, 3]
    if n < 9080191: return [31, 73]
    if n < 25326001: return [2, 3, 5]
    if n < 4759123141: return [2, 7, 61]
    return [2, 3, 5, 7, 11]

check = [n for n in primes2(100)][1:]
def miller_rabin(n, test=None):
    for p in check:
        if not n%p: return False
    if not test: test = [2, 3, 5]
    s = 0
    d = n - 1
    while not d % 2:
        s += 1
        d //= 2

    for a in test:
        for i in range(s):
            x = pow(a, d*2**i, n)
            if x == n - 1 or x == 1: break
            for _ in range(s):
                x = x**2 % n
                if x == 1: return False
                if x == n - 1: break
            else:
                return False
    return True


def miller_rabin_range(n, t=500000):
    test = get_test_list(n)
    for p in primes2(t): yield p
    for x in range(t+1, n, 2):
        if miller_rabin(x, test): yield x

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b
