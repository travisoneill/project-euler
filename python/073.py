from math import ceil
from primesandfactors import prime_factors, primes2
from benchmark import benchmark

primes = {p for  p in primes2(12000)}

def fracs(n):
    factors = prime_factors(n)
    start = ceil(n / 3)
    end = n // 2
    for i in range(start, end+1):
        if i == 1:
            yield 1
            continue
        if i in primes and n % i:
            yield i
            continue
        for f in factors:
            if i % f == 0:
                break
        else:
            yield i


@benchmark()
def fracs_in_range(n):
    count = 0
    for i in range(2, n+1):
        for f in fracs(i):
            count += 1
    return count - 2 # exclute 1/2 and 1/3


if __name__ == '__main__':
    print(fracs_in_range(12000))
