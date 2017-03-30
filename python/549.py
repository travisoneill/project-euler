from primesandfactors import prime_factors
from generators import miller_rabin_range
from benchmark import benchmark
from numpy import array

lowest_factorial_multiple = lambda n: max( ( f(v, k) for k, v in prime_factors(n, 'dictionary').items() ) )

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

@benchmark()
def run(n):
    done = array( [True] * (n+1) )
    total = count = 0
    for prime in miller_rabin_range(n+1):
        y = min(n//prime, prime)
        total += prime * (y-1)
        for x in range(1, y):
            done[prime*x] = False
        count += 1
        if not count % 1000000: print(count // 1000000)
    for i in range(2, n+1):
        if not i % 1000000: print(i, total)
        if done[i]: total += lowest_factorial_multiple(i)
    print(total)
