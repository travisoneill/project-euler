from collections import Counter
from simplemath import int_sqrt
from functools import reduce

def is_prime(n):
    '''Returns bool True if prime False if not.'''
    if n < 2: return False
    divisor = 2
    while divisor * divisor <= n:
        if not n % divisor:
            return False
        else:
            divisor += 1 + divisor % 2
    return True

def prime_factors(n, data_type='list'):
    '''Returns prime factors of 'n' in selected data structure.  In sorted order where applicable.
    Returns 1 member collection of 'n' if prime'''
    data_structures = { 'list': list, 'set': set, 'tuple': tuple, 'dictionary': dict }
    prime_factors = []
    divisor = 2
    while divisor * divisor <= n:
        if not n % divisor:
            prime_factors.append(divisor)
            n //= divisor
        else:
            divisor += 1 + divisor % 2
    if n > 1: prime_factors.append(n)
    if data_type == 'dictionary':
        return dict(Counter(prime_factors))
    else:
        return data_structures[data_type](prime_factors)

def all_factors(n, data_type='list', duplicate_sqrt=False, include_self=False):
    '''Returns all factors in selected data structure.  In sorted order where applicable.'''
    data_structures = { 'list': list, 'set': set, 'tuple': tuple}
    factors = []
    divisor = 1 if include_self else 2
    while divisor * divisor <= n:
        if not n % divisor:
            factors.append(divisor)
            if n // divisor != divisor or duplicate_sqrt:
                factors.append(n // divisor)
        divisor += 1
    return data_structures[data_type](sorted(factors))

def are_coprime(n1, n2):
    if n1 == 1 or n2 == 1: return True
    small = min(n1, n2)
    large = max(n1, n2)
    if not large % small: return False
    for p in primes2(small // 2):
        if not n1 % p and not n2 % p: return False
    return True

def primes2(limit):
    '''Generates prime numbers up to limit.  Pass 'None' as argument to infinite loop'''
    if limit < 4:
        sieve = [2, 3]
    else:
        sieve = [ n for n in primes2( int_sqrt(limit) ) ]
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

check = [ n for n in range(100) if is_prime(n) ]
def get_test_list(n):
    if n < 2047: return (2,)
    if n < 1373653: return (2, 3)
    if n < 9080191: return (31, 73)
    if n < 25326001: return (2, 3, 5)
    if n < 4759123141: return (2, 7, 61)
    return (2, 3, 5, 7, 11)

def miller_rabin(n):
    if n < 100:
        return is_prime(n)
    for p in check:
        if not n%p: return False
    test = get_test_list(n)
    s = 0
    d = n - 1
    while not d % 2:
        s += 1
        d //= 2

    for idx, a in enumerate(test):
        p = 1
        for idx2 in range(s):
            x = pow(a, d*p, n)
            if x == n - 1 or x == 1: break
            for _ in range(s):
                x = x*x % n
                if x == 1: return False
                if x == n - 1: break
            else:
                return False
        p <<= 1
    return True

def least_common_mult(n1, n2):
    n1, n2 = sorted([n1, n2])
    factors = prime_factors(n1)
    mult = n1 * n2
    for f in factors:
        if not n2 % f:
            mult //= f
    return mult
