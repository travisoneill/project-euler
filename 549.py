from primesandfactors import prime_factors, is_prime
from generators import primes, primes2, miller_rabin, mr2
from benchmark import benchmark
from collections import defaultdict
from math import sqrt
from numpy import array

# TODO: Prime builder
# lowest_factorial_multiple = lambda n: max([ k*v for k, v in prime_factors(n, 'dictionary').items() ])
lowest_factorial_multiple = lambda n: max( ( f(v, k) for k, v in prime_factors(n, 'dictionary').items() ) )
lfm = lowest_factorial_multiple

def pf(n):
    prime_factors = []
    x = 1
    while not x % 2:
        x *= 2
        n //= 2
    if x > 1: prime_factors.append(x)
    divisor = 3
    while divisor * divisor <= n:
        x = 1
        while not n % divisor:
            x *= divisor
            n //= divisor
        # print(x)
        if x > 1: prime_factors.append(x)
        divisor += 1
    if n > 1: prime_factors.append(n)
    return prime_factors or [n]

@benchmark()
def s(n):
    cache = build_cache(n)
    lowest_factorial_multiple = lambda p, exp: cache[p][exp] if p in cache else p * exp
    total = 0
    for i in range(2, n+1):
        # is_prime(i)
        # total += cache[2][11]
        total += max( lowest_factorial_multiple(k, v) for k, v in prime_factors(i, 'dictionary').items() )
    return total

def f(n, b):
    m = n
    total = 0
    while n > 0:
        i, e = 0, 0
        while True:
            x = b**e
            if i + x > n: break
            i += x
            e += 1
        n -= i
        total += x
    return total


def build_cache(n):
    cache = {}
    limit = 1
    while limit**(limit+1) < n:
        limit += 1
    print(limit)
    for p in primes(limit):
        cache[p] = {}
        exp = 1
        while p**exp <= n:
            cache[p][exp] = f(exp, p)
            exp += 1
    return cache




def build_cache2(n):
    possible_factors = []
    limit = 1
    for p in primes2( int(sqrt(n)) ):
        x = p
        while p <= n:
            possible_factors.append( (p, lfm(p)) )
            p *= x
    print(possible_factors)
    for p in primes2(n):
        if p > int( sqrt(n) ): possible_factors.append( (p, p) )
    print(possible_factors)
    return sorted(possible_factors, key=lambda tup: tup[1])

def score(lst, limit):
    total = 0
    for i in range(len(lst)):
        a, b = lst[i]
        x = min(i+1, limit // a)
        total += b*x
    return total


@benchmark()
def test(n, t=500000):
    [x for x in mr2(n, t)]

@benchmark()
def test2(n):
    [ x for x in primes2(n) ]

@benchmark()
def test3(n):
    [x for x in range(5, n, 2) if mr_prime(x)]

@benchmark(1000)
def test4(b, e, mod):
    x = mod_exp(b, e, mod)

def run(n, t):
    total = s(t)
    for p in primes2(n+1):
        if p > t: total += p * min((n // p), p)
    # print(total)
    return total

@benchmark()
def run2(n):
    d = array([True]*(n+1))
    total = 0
    count = 0
    for pr in mr2(n+1):
        y = min(n//pr, pr)
        total += pr * (y-1)
        for x in range(1, y):
            d[pr*x] = False
        count += 1
        if not count % 1000000: print(count // 1000000)
        # total += pr*(y-1)
    #         count += 1
    # print(count)
    # print(sum(d.values()))
    # print(total)
    print("HERE")
    for i in range(2, n+1):
        if not i % 100000: print(i)
        if d[i]: total += lfm(i)
    print(total)

def run3(n):
    total = 0
    split = int( (4*n)**(1/3) ) + 1
    for i in range( 2, int(sqrt(n))+1 ):
        total += lfm(i)
    for i in range(int(sqrt(n))+1, n+1):
        total += lfm( max( pf(i) ) )
        if lfm( max( pf(i) ) ) != lfm(i): print(i)
    return total

@benchmark()
def run4(n):
    total = 0
    for i in range( 2, 500000 ):
        if is_prime(i):
            total += i
        else:
            total += lfm(i)
    for i in range(500000, n+1):
        if miller_rabin(i, test=[2,7,61]):
            total += i
        else:
            total += lfm(i)
    return total



{10**7: 5494373412573}


def mrtest(x):
    return [2,3,5,7,11,13] + [n for n in range(3, x, 2) if  miller_rabin(n)] == [n for n in primes2(x)]
    # return [n for n in mr2(x)] == [n for n in primes2(x)]
