from collections import Counter
from benchmark import benchmark
from primesandfactors import are_coprime

def euclid_sum(m, n):
    return 2 * m * (m + n)

@benchmark()
def side_length_triples(limit):
    euclid_max = 1
    while euclid_sum(euclid_max, 1) < limit:
        euclid_max += 1
    print(euclid_max)
    triple_perimeters = Counter()
    for n in range(1, euclid_max+1):
        for m in range(n+1, euclid_max+1):
            if not bool(m % 2) ^ bool(n % 2): continue
            if not are_coprime(m, n): continue
            perimeter = euclid_sum(m, n)
            val = perimeter
            while val <= limit:
                triple_perimeters[val] += 1
                val += perimeter
    return len([ x for x in triple_perimeters if triple_perimeters[x] < 2 ])

#CLI shorthand
sl = side_length_triples
