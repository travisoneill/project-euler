from generators import primes
from benchmark import benchmark

@benchmark()
def run(x):
    primes4 = [ n**4 for n in primes(x**(1/4)) ]
    primes3 = [ n**3 for n in primes(x**(1/3)) ]
    primes2 = [ n**2 for n in primes(x**(1/2)) ]
    result = set()
    for p4 in primes4:
        for p3 in primes3:
            if p4 + p3 > x: continue
            for p2 in primes2:
                if p2 + p3 + p4 < x: result.add(p2+p3+p4)
    print(len(result))
