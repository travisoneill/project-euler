from itertools import combinations
from collections import defaultdict
from generators import primes2

def replace(n, digit, replacement):
    digit = 10**digit
    return (digit*10) * (n // (digit*10)) + replacement * digit + n % digit

def handle(family, prime, digits):
    result = []
    missing = set()
    for i in range(digits):
        digit = (prime // 10**i) % 10
        if i in family:
            result.append(digit)
        else:
            missing.add(digit)
    if len(missing) == 1:
        return tuple(result)

def prime_families(digits, replacements, target_length):
    dd_list = lambda: defaultdict(list)
    result = defaultdict(dd_list)
    families = list( map( lambda tup: (0,) + tup, combinations( [ n for n in range(1, digits) ], digits-replacements-1 ) ) )
    print('Searching {} digit primes with {} replacements'.format(digits, replacements))
    for prime in primes2(10**(digits)):
        if prime < 10**(digits-1): continue
        for family in families:
            entry = handle(family, prime, digits)
            if entry:
                result[family][entry].append(prime)
                if len(result[family][entry]) == target_length: return result[family][entry]

# def search(dictionary, target_length):
#     for k1, v1 in dictionary.items():
#         for k2, v2 in v1.items():
#             if len(v2) >= target_length:
#                 print(k1, k2, v2)

def run(target_length):
    digits = 1
    while True:
        for replacements in range(1, digits):
            x = prime_families(digits, replacements, target_length)
            if x: return x
        digits += 1
