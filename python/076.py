from benchmark import benchmark
import sys
import math

def gen_seq(n):
    jump = 1
    gap = 1
    while True:
        o1, o2 = n - jump, n - jump - gap
        if o1 > -1: yield o1
        else: break
        if o2 > -1: yield o2
        else: break
        jump += 2
        gap += 1
        n = o2

@benchmark()
def num_partitions(n, mod=math.inf, cache=None):
    if cache is None: cache = [1,1]
    i = len(cache)
    while i <= n:
        parts = 0
        for iter, x in enumerate(gen_seq(i)):
            parts += cache[x] * (1 - 2*int(iter % 4 > 1))
        cache.append(int(parts % mod))
        if parts % mod == 0:
            break
        i += 1
    return cache


def main(n, mod):
    for i, n in enumerate(num_partitions(n, mod)):
        if n % mod == 0:
            print(i, n)

if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
    
