from benchmark import benchmark
from primesandfactors import primes2

@benchmark()
def gen(lim):
    count = 0
    d4 = lim // 4
    d16 = lim // 16
    for p in primes2(lim):
        count += int(p % 4 == 3) + int(p <= d4) + int(p <= d16)
    return count
