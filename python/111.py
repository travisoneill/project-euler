from math import factorial
from itertools import permutations
from primesandfactors import is_prime

def n_without(n, digits):
    limit = 10**digits
    i = 0
    while i < limit:
        for d in range(digits):
            if (i//(10**d)) % 10 == n:
                i += 10**d
        if i >= limit: break
        yield i
        i += 1

def fill(template, digit):
    limit = len(template) - sum(template)
    for n in n_without(digit, limit):
        num = 0
        for x in template:
            num *= 10
            if x:
                num += digit
            else:
                num += n%10
                n //= 10
        yield num

def possibilities(n, d):
    repeat = True
    for i in range(10):
        if not repeat: break
        t = [True] * (n-i) + [False] * i
        print('__________')
        for p in set(permutations(t)):
            for x in fill(p, d):
                if is_prime(x) and x > 10**(n-1):
                    repeat = False
                    print(x)
                    yield(x)

def run(n):
    result = 0
    for d in range(10):
        for p in possibilities(n, d):
            result += p
    print(result)

def bm(n):
    from time import time
    t0 = time()
    run(n)
    t1 = time()
    print(t1-t0)
