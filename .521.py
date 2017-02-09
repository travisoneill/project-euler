from generators import primes2
from primesandfactors import prime_factors

def run(limit):
    start = [1]
    p = 2
    for prime in primes2(11):
        if prime == 2: continue


def steps(n):
    a, b, c = 1, 2, 4
    step = 3
    while step < n:
        a, b, c = b, c, a+b+c
        step += 1
    return c

def steps2(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return steps2(n-1) + steps2(n-2) + steps2(n-3)


arr = [-3, 1, 3, 4, 5, 6, 7, 8, 15, 20]
arr = [0,1,2,3,4,5,7,8,9,10]
arr = [-5,-4,3,5,7,8,9,10]

def magic(arr):
    lo, hi = 0, len(arr) - 1
    while hi - lo > 1:
        mid = (hi + lo) // 2
        test = mid - arr[mid]
        if not test:
            break
        elif test < 0:
            hi = mid
        else:
            lo = mid

    count = 0
    search = mid
    while not search - arr[search]:
        count += 1
        search += 1
    search = mid - 1
    while not search - arr[search]:
        count += 1
        search -= 1
    return count

def m_primes(n):
    f = set(prime_factors(n))
    m = []
    for i in range(1, n):
        if not set(prime_factors(i)) & f:
            m.append(i)
    return m

def generate(n, limit):
    yield n
    yield n**2
    exponents = [n, n**2]
    power = 3
    for p in primes2(limit):
        if p <= n: continue
        if n*p > n**power:
            print(n, p, power)
            if n**power <= limit:
                yield n**power
                exponents.append(n**power)
            power += 1
        for exp in exponents:
            if p * exp > limit: break
            yield p * exp

def g2(n, limit):
    cycle_length = 1
    for p in primes2(n-1):
        cycle_length *= p
    if n == 3: cycle_length = 2
    cycle = m_primes(cycle_length)
    print(cycle, cycle_length)
    for i in range(n, limit+1, n):
        if i % cycle_length in cycle:
            yield i

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

def subc(sett):
    for n in range(2**(len(s))):
        pass
