from time import time

# ONE LINER
problem48 = lambda n: sum([i**i % 10**10 for i in range(1, n+1)]) % 10**10


# slower than brute force for smaller numbers but becomes more efficient for larger numbers
def last_10(base, exponent):
    mod = 10**10
    result = 1
    for _ in range(exponent):
        result *= base
        result %= mod
    return result

def run(n):
    s = 0
    for i in range(1, n+1):
        s += last_10(i, i)
    return s % 10**10

# BRUTE FORCE
def brute_force(n):
    s = 0
    for i in range(1, n+1):
        s += i**i
        return s % 10**10

# BENCHMARK
def bm(f, n):
    t0 = time()
    f(n)
    t1 = time()
    print(t1-t0)

def benchmark(n):
    bm(brute_force, n)
    bm(p48, n)
    bm(run, n)
