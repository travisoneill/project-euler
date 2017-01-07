from math import sqrt
from functools import reduce
from benchmark import benchmark

trip = lambda n: ( (a, int(sqrt(c**2 - a**2)), c) for a in range(1, int(0.3*n+1)) for c in range(int(0.4*n), int(0.5*n+1)) if (c**2 - a**2) % 1 == 0 and (a + sqrt(c**2 - a**2) + c) == n )
trip2 = lambda n: { tuple(sorted([a, int(sqrt(c**2 - a**2)), c])) for a in range(1, int(1+3*n//10)) for c in range(int(4*n//10), int(1+5*n//10)) if (a + sqrt(c**2 - a**2) + c) == n }
ptrip = lambda n: { (a, int(sqrt(c**2 - a**2)), c) for a in range(1, int(0.3*n+1)) for c in range(int(0.4*n), int(0.5*n+1)) if (c**2 - a**2) % 1 == 0 and (a + sqrt(c**2 - a**2) + c) == n and prim( (a, sqrt(c**2 - a**2), c) ) }

from time import time
def get_triples(limit):
    skip = []
    triples = set()
    t0 = time()
    for i in range(0, limit, 2):
        state = True
        for n in skip:
            if i % n == 0:
                state = False
                break
        if not state: continue
        if not i % 1000: print(i, time() - t0)
        for t in trip3(i):
            triples.add(t)
            skip.append(sum(t))
    return triples


# @benchmark()
def trip3(n):
    triples = set()
    for a in range(1, int(1+3*n//10), 2):
        for c in range(int(4*n//10)+1, int(1+5*n//10), 2):
            b = sqrt(c**2 - a**2)
            if a+b+c == n:
                triples.add( tuple(sorted([a, int(b), c])) )
    return triples


def int_sqrt(n):
    lo, hi = 1, n
    while hi - lo > 1:
        mid = (hi + lo) // 2
        val = mid * mid
        if val == n: return mid
        if val > n: hi = mid
        if val < n: lo = mid
    return None

def score(triple, m):
    a, b, c = triple
    score = 0
    if  a > m or b > 2*m or a+b > 3*m: return score
    score += int(a - b / 2) + 1
    if b <= m:
        score += a // 2
    return score

def run(n):
    total = 0
    for t in get_triples(n):
        total += score(t, n)
    print(total)

def find(start, nd):
    m = 0
    n = 0
    for i in range(start, nd, 2):
        p = ptrip(i)
        l = len(p)
        if l > m:
            m = l
            n = i
            # print(p, n)
        if l > 0:
            print(p, i)
    # print(m, n)

def factors(n):
    if n == 1: return 1
    f = set()
    i = 2
    while i <= sqrt(n):
        if n%i == 0:
            f.add(i)
            n //= i
        else:
            i += i%2 + 1
    if n > 1: f.add(n)
    return f

def prim(trip):
    f = factors(trip[0])
    for n in f:
        if trip[1] % n == 0 and trip[2] % n == 0:
            return False
    return True

d = {
    1716: [ (195, 748, 773), (364, 627, 725) ],
    2652: [ (51, 1300, 1301), (340, 1131, 1181) ],
    3876: [ (627, 1564, 1685), (988, 1275, 1613) ],
    3960: [ (88, 1935, 1937), (935, 1368, 1657) ],
    4290: [ (1248, 1265, 1777), (65, 2112, 2113) ],
    5244: [ (483, 2356, 2405), (1012, 1995, 2237) ],
    5700: [ (75, 2812, 2813), (700, 2451, 2549) ],
    5720: [ (312, 2695, 2713), (1495, 1848, 2377) ],
    6900: [ (1275, 2668, 2957), (1900, 2139, 2861) ],
    6930: [ (880, 2961, 3089), (1001, 2880, 3049) ],
    8004: [ (435, 3772, 3797), (1276, 3243, 3485) ],
    8700: [ (1131, 3700, 3869), (1972, 3075, 3653) ],
    9300: [ (651, 4300, 4349), (1612, 3675, 4013) ],
    9690: [ (2465, 3192, 4033), (665, 4488, 4537) ],
    10010: [ (1560, 4081, 4369), (1729, 3960, 4321) ]
}
