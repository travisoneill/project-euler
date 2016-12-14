from euler_utils_primesandfactors import is_prime
# f = lambda n, a, b: n**2 + a*n + b

quadratic = lambda a, b: eval('lambda n: n**2 + {}*n + {}'.format(a, b))

quadratic = lambda a, b, n: n**2 + a*n + b



def run(limit):
    primes = {}
    def primetest(n):
        if n in primes:
            return primes[n]
        else:
            primes[n] = is_prime(n)
            return primes[n]

    def test(a, b):
        count, n = 0, 0
        while primetest(quadratic(a, b, n)):
            n, count = n+1, count+1
        return count

    longest = 0
    best_a, best_b = None, None
    for b in range(1, limit+1):
        if not primetest(b): continue
        for a in range(-limit, limit+1):
            if not a%2: continue
            p1, p2 = quadratic(a, b, longest), quadratic(a,b,longest-1)
            if primetest(p1) and primetest(p2):
                t = test(a, b)
                if(t > longest):
                    longest = t
                    best_a, best_b = a, b
    print(best_a, best_b, longest)
    return best_a * best_b

from time import time
def bm(n):
    t0 = time()
    run(n)
    t1 = time()
    print(t1-t0)
