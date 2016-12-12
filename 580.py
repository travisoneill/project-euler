from euler_utils_primesandfactors import prime_factors

hilbert = lambda n: 4*n+1
hilbert_square = lambda n: 16*n**2 + 8*n + 1

is_hilbert = lambda n: n % 4 == 1

for n in range(10): print(hilbert(n), hilbert_square(n))

first_thousand = [ hilbert(n) for n in range(1, 1001) ]

from time import time
def iter_time(n):
    t0 = time()
    i = 0
    while i < n:
        i += 1
    t1 = time()
    print(t1-t0)

for i in range(1001):
    print(hilbert(i) % 25)
    # print(prime_factors(hilbert(i)))

hilbert_mod = lambda divisor, limit: [ hilbert(i) % divisor for i in range(limit+1) ]

def find_cycle(lst):
    cycle = 1
    while cycle < len(lst):
        for i in range(len(lst) - cycle):
            if lst[i] != lst[i + cycle]:
                break
        else:
            return cycle
        cycle += 1


for n in range(2, 1000):
    if not is_hilbert(n): continue
    h = hilbert_mod(n, 2000)
    c = find_cycle(h)
    d = 0 in h
    print(n, c, c/n, d)
