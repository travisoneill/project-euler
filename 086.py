from math import sqrt
trip = lambda n: ( (a, int(sqrt(c**2 - a**2)), c) for a in range(1, int(0.3*n+1)) for c in range(int(0.4*n), int(0.5*n+1)) if (c**2 - a**2) % 1 == 0 and (a + sqrt(c**2 - a**2) + c) == n )
trip2 = lambda n: { tuple(sorted([a, int(sqrt(c**2 - a**2)), c])) for a in range(1, int(1+3*n//10)) for c in range(int(4*n//10), int(1+5*n//10)) if (a + sqrt(c**2 - a**2) + c) == n }
ptrip = lambda n: { (a, int(sqrt(c**2 - a**2)), c) for a in range(1, int(0.3*n+1)) for c in range(int(0.4*n), int(0.5*n+1)) if (c**2 - a**2) % 1 == 0 and (a + sqrt(c**2 - a**2) + c) == n and prim( (a, sqrt(c**2 - a**2), c) ) }

from time import time
def get_triples(limit):
    t0 = time()
    triples = set()
    for i in range(limit*6):
        for t in trip3(i):
            triples.add(t)
    print(time() - t0)
    return triples

def trip3(n):
    triples = set()
    for a in range(1, int(1+3*n//10)):
        for c in range(int(4*n//10), int(1+5*n//10)):
            b = sqrt(c**2 - a**2)
            if a+b+c == n:
                triples.add( tuple(sorted([a, int(b), c])) )
    return triples

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
