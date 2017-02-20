from benchmark import benchmark
from primesandfactors import miller_rabin

@benchmark()
def run(ratio):
    n = 1
    corner = 0
    step = 0
    total = 0
    primes = 0
    while True:
        total += 1
        if total % 4 != 1:
            primes += miller_rabin(n)
        if primes and primes * ratio < total: break
        if not corner % 4:
            step += 2
        corner += 1
        n += step
    side_length = step + 1
    print(side_length)
