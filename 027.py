from euler_utils_primesandfactors import is_prime
from collections import defaultdict
# f = lambda n, a, b: n**2 + a*n + b

quadratic = lambda a, b: eval('lambda n: n**2 + {}*n + {}'.format(a, b))

def run(limit):
    primes = defaultdict(lambda: False, { n: True for n in range(limit*2) if is_prime(n) })

    def test(func):
        count, n = 0, 0
        while primes[func(n)]:
            n, count = n+1, count+1
        return count

    longest = 40
    for b in reversed(list(primes.keys())):
        if b > limit: continue
        for a in range(-limit, limit+1):
            f = quadratic(a, b)
            if primes[f(longest)] and primes[f(longest-1)]:
                t = test(f)
                if(t > longest): print(a, b, t)
                longest = max(longest, t)
