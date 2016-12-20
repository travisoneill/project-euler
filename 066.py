from math import sqrt
from primesandfactors import prime_factors

def minimal(n):
    if sqrt(n) % 1 == 0: return 0
    i = 1
    while True:
        if sqrt(n*i**2 + 1) % 1 == 0:
            # print(i)
            return int(sqrt(n*i**2 + 1))
        i += 1

def get_max(n):
    mx = 0
    for i in range(n+1):
        x = minimal(i)
        mx = max(mx, x)
        print(i, x)
