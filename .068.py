from math import factorial
from itertools import combinations, permutations
from benchmark import benchmark

@benchmark()
def possibilities_for_ring_size(n):
    nums = [ x+1 for x in range(n*2) ]
    inner_ring = combinations(nums, n)
    seen = set()
    for ring in inner_ring:
        outer = tuple( x for x in nums if x not in ring )
        for o in permutations(outer):
            for r in permutations(ring):
                t = test(r, o)
                if t:
                    p = print_format(r, o)
                    if p not in seen:
                        print(p)
                    seen.add(p)

def print_format(ring, outer):
    arr = []
    result = ''
    start_idx = 0
    for i in range(0, len(ring)):
        j = (i + 1) % len(ring)
        t = (outer[i], ring[i], ring[j])
        if t[0] == min(outer): start_idx = i
        arr.append(t)
    for i in range(len(arr)):
        idx = (start_idx + i) % len(arr)
        for n in arr[idx]:
            result += str(n)
    return result

def test(center, outer):
    summ = 0
    for i in range(0, len(center)):
        j = (i + 1) % len(center)
        t = outer[i] + center[i] + center[j]
        summ = summ or t
        if t != summ: return False
    return summ
