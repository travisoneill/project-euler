from math import sqrt
from functools import reduce
from itertools import combinations

def f_set(n):
    i = 2
    factors = set()
    # prime = True
    while i < int(sqrt(n)) + 1:
        if n % i == 0:
            # prime = False
            factors.add(i)
            n //= i
        else:
            i += 1
    # if prime: return set()
    if n > 1: factors.add(n)
    return factors

def set_perm(s):
    perms = set()
    for n in range(2, len(s) + 1):
        for m in combinations(s, n):
            perms.add(reduce(lambda x, y: x*y, m))
    # print(perms)
    return perms

def f_range(x, m):
    s = f_set(x)
    p = set_perm(s)
    r = m - x
    # a = r
    for n in s:
        d = m//n - x//n
        # print(m, x, n)
        # print(d)
        r -= d
    # print(x)
    for n in p:
        d = m//n - x//n
        r += d
    # print(r)
    return r

def run(n):
    count = 0
    for i in range(1, n):
        count += f_range(i, n)
    print(count)

failures = {
    60: 2,
    84, 2,
    90: 4,
    120: 6,
    150: 8,
}
