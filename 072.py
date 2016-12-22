from primesandfactors import prime_factors
from itertools import combinations
from functools import reduce
from generators import primes

product = lambda collection: reduce(lambda x, y: x*y, collection)
c_prod = lambda factors, n: set(map(product, combinations(factors, n)))

cache = {}
def phi(n):
    f = prime_factors(n)
    if len(f) == 1:
        cache[n] = n-1
        return n-1
    family = product(set(f))
    if family > 1 and family in cache:
        cache[n] = cache[family] * n // family
        return cache[n]

    f = set(f)
    idx = n - 1
    for i in range(len(f)):
        multiplier = [-1, 1]
        c = c_prod(f, i+1)
        for x in c:
            idx += (n//x - 1) * multiplier[i%2]
    cache[n] = idx
    return idx

def run(n):
    s = 0
    for n in range(2, n+1):
        s += phi(n)
    return s
