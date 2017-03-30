from primesandfactors import prime_factors
from itertools import combinations
from functools import reduce
from generators import primes

product = lambda collection: reduce(lambda x, y: x*y, collection)
c_prod = lambda factors, n: set(map(product, combinations(factors, n)))

def phi(n, limit=None):
    idx = n - 1
    f = prime_factors(n, 'set')
    if limit and len(f) > limit: return n//2
    for i in range(len(f)):
        multiplier = [-1, 1]
        c = c_prod(f, i+1)
        for x in c:
            idx += (n//x - 1) * multiplier[i%2]
    return idx

def is_perm(n1, n2):
    idx = [0] * 10
    while n2 > 0 and n1 > 0:
        idx[n1 % 10] += 1
        idx[n2 % 10] -= 1
        n1 //= 10
        n2 //= 10
    return not n1 and not n2 and not [n for n in idx if n != 0]

def run(n):
    r_min = 5
    pr = [n for n in primes(100)]
    for i in range(1, n, 2):
        if not (i%3 and i%5 and i%7 and i%11 and i%13 and i%17 and i%23 and i%29):
            continue
        p = phi(i, 2)
        if is_perm(i, p):
            r = i / p
            if r < r_min:
                r_min = r
                print(i, p, r)
