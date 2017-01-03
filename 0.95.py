from primesandfactors import prime_factors
from benchmark import benchmark

def fast_sum_divisors(n):
    product = 1
    for factor, power in prime_factors(n, 'dictionary').items():
        term = 1
        for i in range(1, power+1):
            term += factor**i
        product *= term
    return product - n

def amicable_chain(n, limit=None):
    seen = set()
    valid = False
    m = n
    while n not in seen:
        seen.add(n)
        n = cache[n]
        if limit and n > limit: break
    if n == m: valid = True
    return { 'valid': valid, 'chain': seen, 'terminal': n, 'length': len(seen) }

def chains_less_than(limit):
    chains = []
    chain_lengths = {}
    for i in range(limit):
        if i in chain_lengths: continue
        j = i
        while j not in chain_lengths and j < limit and j > 1:
            chain_lengths[j] = 0
            j = cache[j]
        if j < limit and j > 1 and not chain_lengths[j]:
            chain = amicable_chain(j, limit)
            if chain['valid']:
                chains.append(chain['chain'])
                for x in chain['chain']:
                    chain_lengths[x] = chain['length']
    return chains

cache = {}
@benchmark()
def run(n):
    for i in range(n):
        cache[i] = fast_sum_divisors(i)
    chains = chains_less_than(n)
    print( min(sorted(chains, key=len)[-1]) )
