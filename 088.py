from itertools import permutations, combinations
from functools import reduce
from collections import defaultdict

def prime_factors(n):
    i = 2
    f = []
    while i * i <= n:
        if not n%i:
            f.append(i)
            n //= i
        else:
            i += 1 + i % 2
    if n > 1: f.append(n)
    return f

# Returns number for which a set of factors is a product-sum number
value = lambda fact_set: reduce(lambda x, y: x*y, fact_set) - sum(fact_set) + len(fact_set)

def construct(n):
    cache = {}
    result = defaultdict(lambda: None)
    count = 0
    i = 2
    while count < n:
        # print(i, n-1, count)
        p = prime_factors(i)
        if len(p) == 1:
            cache[i] = [(p[0],)]
        else:
            f = p[0]
            combs = cache[i//f]
            res = set()
            for tup in combs:
                res.add( tuple(sorted(list(tup + (f,)))) )
                # if len(tup) == 1: continue
                for j in range(len(tup)):
                    lst = list(tup[:])
                    lst[j] *= f
                    lst.sort()
                    res.add(tuple(lst))
            for tup in res:
                v = value(tup)
                if v <= n and not result[v]:
                    result[v] = i
                    count += 1
            cache[i] = list(res)
        i += 1
    # print(cache)
    return result

def add_factor():
    pass


def run(n):
    d = construct(n)
    print(sum(set(d.values())))
    return sum(set(d.values()))




def run2(n):
    d = defaultdict(lambda: None)
    count = 0
    i = 2
    while count < n - 1:
        for diff in mapper(all_combs(i)):
            if not d[diff] and diff <= n:
                d[diff] = i
                count += 1
        i += 1
    # for n in range(2, n+1):
    #     for diff in mapper(all_combs(n)):
    #         d[diff].append(n)
    return d

def all_combs(n):
    if n <= 1: return
    return helper((), n, n)

def helper(currExpression, dividend, previousFactor, res=None):
    res = res or []
    for factor in reversed(range(2, dividend)):
        if dividend % factor == 0 and factor <= previousFactor:
            nextFactor = dividend // factor
            if nextFactor <= factor:
                # print( currExpression + [factor] + [nextFactor] )
                res.append( currExpression + (factor, nextFactor) )
            helper((currExpression) + (factor,), nextFactor, factor, res)
    return res

def bm(n):
    from time import time
    t0 = time()
    run(n)
    t1 = time()
    print(t1-t0)

def bm2(n):
    from time import time
    t0 = time()
    run2(n)
    t1 = time()
    print(t1-t0)
