from math import sqrt, factorial
from time import time
n = 600851475143

def max_factor(n):
    max_factor = 1
    i = 2
    while i < sqrt(n) + 1:
        if n % i == 0:
            if i > max_factor: max_factor = i
            n //= i
        else: i += 1
    if n > max_factor: max_factor = n
    print(max_factor)

#BENCHMARK
# def bm(f, n):
#     t0 = time()
#     for _ in range(100):
#         f(n)
#     t1 = time()
#     print(t1-t0)
#
# bm(max_factor, n)
