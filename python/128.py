from primesandfactors import is_prime
from math import sqrt

hex_end = lambda n: 3*n**2 + 3*n + 1
hex_start = lambda n: 3*n**2 - 3*n + 2
hex_level = lambda n: int( (sqrt(12*n - 15) + 3 ) // 6 )

get_index = lambda n: ( hex_level(n), n - hex_start(hex_level(n)) )
get_value = lambda tup: hex_start(tup[0]) + tup[1]

def get_neighbors(val):
    idx = get_index(val)
    ring = idx[0]
    position = idx[1]
    ring_length = ring * 6
    next_position = (position + 1) % ring_length
    prev_position = (position - 1) % ring_length
    next_door = [(ring, next_position), (ring, prev_position)]
    inner = []
    outer = []
    inner_idx = (position * (ring-1)) / ring
    outer_idx = (position * (ring+1)) / ring
    inner.append( ( ring-1, int(inner_idx) ) )
    outer.append( ( ring+1, int(outer_idx) ) )
    outer.append( ( ring+1, int(outer_idx +1) % (ring_length+6) ) )
    # If corner
    if inner_idx % 1 == 0:
        outer.append( ( ring+1, int(outer_idx-1) % (ring_length+6) ) )
    else:
        inner.append( ( ring-1, int(inner_idx+1) % (ring_length-6) ) )
    neighbors = inner + next_door + outer
    values = list(map(get_value, neighbors))
    return values

def prime_diffs(n):
    neighbors = get_neighbors(n)
    count = 0
    for neighbor in neighbors:
        if is_prime(abs(n - neighbor)): count += 1
    return count

def run(n):
    ring_level = 2
    count = 2 # for 1 and 2 whicha have PD = 3 in level 1
    while True:
        nd = hex_end(ring_level)
        start = hex_start(ring_level)
        # Search corners
        for i in range(start, nd, ring_level):
            if prime_diffs(i) == 3:
                count += 1
            if count == n: return i
        # Check end
        if prime_diffs(nd) == 3:
            count += 1
        if count == n: return nd
        ring_level += 1

# Benchmark
from time import time
def bm(n):
    t0 = time()
    run(n)
    t1 = time()
    print(t1-t0)
