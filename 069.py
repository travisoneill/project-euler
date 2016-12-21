from primesandfactors import prime_factors, all_factors
from itertools import combinations
from functools import reduce
from generators import primes

def greatest_phi_ratio_under(n):
    x = 1
    for p in primes(None):
        if x * p > n: break
        x *= p
    return x

product = lambda collection: reduce(lambda x, y: x*y, collection)

def all_prod(n):
    factors = prime_factors(n, 'set')
    all_factors = set()
    for i in range(1, len(factors)):
        for tup in combinations(factors, i):
            all_factors.add(product(tup))
    return all_factors

def phi2(n):
    idx = [True] * n
    for f in all_prod(n):
        for i in range(0, n, f):
            if i % f == 0:
                idx[i] = False
    print(sum(idx))
    return   n / sum(idx)
