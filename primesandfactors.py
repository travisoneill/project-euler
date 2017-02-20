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


check = [ n for n in range(100) if is_prime(n) ]
# def fast_prime(n):
#     if n < 1000:
#         return is_prime(n)
#     # for p in check:
#         # if not n % p: return False
#     else:
#         return miller_rabin(n)
#
#     # if n < 100000:
#         # return is_prime(n)
#     # else:

def get_test_list(n):
    if n < 2047: return [2]
    if n < 1373653: return [2, 3]
    if n < 9080191: return [31, 73]
    if n < 25326001: return [2, 3, 5]
    if n < 4759123141: return [2, 7, 61]
    return [2, 3, 5, 7, 11]

def miller_rabin(n):
    if n < 100:
        return is_prime(n)
    for p in check:
        if not n%p: return False
    test = get_test_list(n)
    s = 0
    d = n - 1
    while not d % 2:
        s += 1
        d //= 2

    for a in test:
        for i in range(s):
            x = pow(a, d*2**i, n)
            if x == n - 1 or x == 1: break
            for _ in range(s):
                x = x**2 % n
                if x == 1: return False
                if x == n - 1: break
            else:
                return False
    return True

def test(n):
    for i in range(n):
        if is_prime(i) != fast_prime(i):
            print(i)
