import math
from benchmark import benchmark
rev_triangular = lambda x: math.sqrt(2*x + 0.25) - 0.5

def L(n):
    max_row = int(rev_triangular(n//8))
    count = 0
    x = n // 4
    for i in range(1, max_row+1):
        if x % i == 0:
            count += 1
    return count


@benchmark()
def N(n, lim):
    count = 0
    for x in range(8, lim+1, 4):
        count += int(L(x) == n)
    print(count)

@benchmark()
def SUM_N(lo, hi, lim):
    count = 0
    for x in range(8, lim+1, 4):
        l = L(x)
        count += int(l >= lo and l <= hi)
    return count
