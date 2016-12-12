from euler_utils_primesandfactors import prime_factors

hilbert = lambda n: 4*n+1
hilbert_square = lambda n: 16*n**2 + 8*n + 1

is_hilbert = lambda n: n % 4 == 1

for n in range(10): print(hilbert(n), hilbert_square(n))

first_thousand = [ hilbert(n) for n in range(1, 1001) ]

def hibbert():
    pass

from time import time
def iter_time(n):
    t0 = time()
    i = 0
    while i < n:
        i += 1
    t1 = time()
    print(t1-t0)

for i in range(1001):
    print(prime_factors(hilbert(i)))
