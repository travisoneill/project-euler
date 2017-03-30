from collections import defaultdict
from functools import reduce

triangular = lambda n: (n**2 + n) // 2
square = lambda n: n**2
pentagonal = lambda n: (3*n**2 - n) // 2
hexagonal = lambda n: 2*n**2 - n
heptagonal = lambda n: (5*n**2 - 3*n) // 2
octagonal = lambda n: 3*n**2 - 2*n

funcs = {
    'triangular': triangular,
    'square': square,
    'pentagonal': pentagonal,
    'hexagonal': hexagonal,
    'heptagonal': heptagonal,
    'octagonal': octagonal
}

def make_options(digits):
    n_map = defaultdict(list)
    for name, f in funcs.items():
        i = 1
        while f(i) < 10**digits:
            if f(i) >= 10**(digits-1):
                n_map[name].append(f(i))
            i += 1
    return n_map

def make_cycles(nums):
    cycles = set()
    for n1 in nums:
        for n2 in [n for n in nums if n//100 == n1% 100]:
            for n3 in [n for n in nums if n//100 == n2% 100]:
                for n4 in [n for n in nums if n//100 == n3% 100]:
                    for n5 in [n for n in nums if n//100 == n4% 100]:
                        for n6 in [n for n in nums if n//100 == n5% 100]:
                            if n6 % 100 == n1 // 100 and len(set([n1,n2,n3,n4,n5,n6])) == 6:
                                cycles.add(tuple(sorted([n1,n2,n3,n4,n5,n6])))
    return cycles

def check(tup, n_map):
    state = {
        'triangular': False,
        'square': False,
        'pentagonal': False,
        'hexagonal': False,
        'heptagonal': False,
        'octagonal': False
    }
    for n in tup:
        for name, lst in n_map.items():
            if n in lst:
                print(name)
                state[name] = True

    return reduce(lambda x, y: x & y, state.values(), True)

def run():
    n_map = make_options(4)
    cycles = make_cycles([v for k, v in n_map.items() for v in v])
    for cycle in cycles:
        if check(cycle, n_map):
            print(cycle)
