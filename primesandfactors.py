from collections import Counter

def is_prime(n):
    '''Returns bool True if prime False if not.'''
    if n < 2: return False
    divisor = 2
    while divisor * divisor <= n:
        if not n % divisor:
            return False
        else:
            divisor += 1 + divisor % 2
    return True

def prime_factors(n, data_type='list'):
    '''Returns prime factors of 'n' in selected data structure.  In sorted order where applicable.
    Returns 1 member collection of 'n' if prime'''
    data_structures = { 'list': list, 'set': set, 'tuple': tuple, 'dictionary': dict }
    prime_factors = []
    divisor = 2
    while divisor * divisor <= n:
        if not n % divisor:
            prime_factors.append(divisor)
            n //= divisor
        else:
            divisor += 1 + divisor % 2
    if n > 1: prime_factors.append(n)
    if data_type == 'dictionary':
        return dict(Counter(prime_factors))
    else:
        return data_structures[data_type](prime_factors)

def all_factors(n, data_type='list', duplicate_sqrt=False, include_self=False):
    '''Returns all factors in selected data structure.  In sorted order where applicable.'''
    data_structures = { 'list': list, 'set': set, 'tuple': tuple}
    factors = []
    divisor = 1 if include_self else 2
    while divisor * divisor <= n:
        if not n % divisor:
            factors.append(divisor)
            if n // divisor != divisor or duplicate_sqrt:
                factors.append(n // divisor)
        divisor += 1
    return data_structures[data_type](sorted(factors))
