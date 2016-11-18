from math import sqrt, log
from functools import reduce

#ONE LINER
print(reduce(lambda a, b: a * b, [n ** int(log(20, n)) for n in (x for x in range(2, 20) if not [y for y in range(2, int(sqrt(x))+1) if x % y == 0])]))

# primes = lambda n: (x for x in range(2, n) if not [y for y in range(2, int(sqrt(x))+1) if x % y == 0])
# x = reduce(lambda a, b: a * b, [n ** int(log(20, n)) for n in primes(20)])
# print(x)


#OLD APPROACH
from collections import defaultdict
def f_count(n):
    count = defaultdict(int, {})
    i = 2
    while i < sqrt(n) + 1:
        if n % i == 0:
            count[i] += 1
            n //= i
        else:
            i += 1
    if n > 1: count[n] += 1
    return count

max_merge = lambda d1, d2: defaultdict(int, {k: max(d1[k], d2[k]) for d in [d1, d2] for k, v in d.items()})

d = defaultdict(int, {})
for n in range(2, 21):
    d = max_merge(d, f_count(n))

# print(d)
