import sys
from collections import defaultdict

from triples import euclid, prim
from benchmark import benchmark

def generate_triples(limit):
    trips = euclid(4*limit)
    trips = [t for t in trips if (t[0] < limit or t[1] < limit) and t[0] + t[1] <= 3 * limit]
    trips = sorted(tuple(sorted(t)) for t in trips)
    trips = [t for t in trips if prim(t)]
    
    length_dict = defaultdict(list)
    for a, b, _ in trips:
        s = a + b
        m = 1
        while s * m <= 3*limit and (a*m <= limit or b*m <= limit):
            length_dict[s*m].append((a*m, b*m))
            m += 1
    return length_dict


def score(perim, leg1, leg2, M):
    tot = 0
    for leg in (leg1, leg2):
        if leg > M:
            continue
        rem = perim - leg
        if rem < leg:
            tot += rem // 2
        elif rem <= leg * 2:
            tot += (2 * leg - rem) // 2 + 1
    return tot


@benchmark()
def main(limit):
    d = generate_triples(limit)
    tot = 0
    for perim, arr in sorted(d.items()):
        for a, b in arr:
            sc = score(perim, a, b, limit)
            # print(a+b, a, b, sc)
            tot += sc
    return tot


if __name__ == '__main__':
    x = main(int(sys.argv[1]))
    print(x)
