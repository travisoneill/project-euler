from time import time
from math import sqrt

def unique(lst):
    if len(set(lst)) == len(lst):
        return lst
    else:
        return None

def check(l, mod):
    n = l[0] * 100 + l[1] * 10 + l[2]
    return n % mod

def number(arr):
    p = 0
    n = 0
    for i in reversed(range(len(arr))):
        n += arr[i] * 10**p
        p += 1
    return n

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    while not is_prime(n+1):
        n += 1
    return n + 1

def make(num, stop):
    if num == stop:
        #ONE LINER
        # [[n//100, n//10 % 10, n%10] for n in range(1, 1000) if n%17 == 0 and len(Counter(str(n))) == len(str(n))]
        #FAST
        n = stop
        while n < 1000:
            l = [n // 100, n // 10 % 10, n % 10]
            if unique(l): yield l
            n += stop
    else:
        for n in make(next_prime(num), stop):
            for i in range(10):
                dig = unique([i] + n)
                if dig and check(dig, num) == 0:
                    yield dig

#RUN
result = 0
for arr in make(1, 17):
    result += number(arr)
print(result)

#BENCHMARK
# def bm():
#     t0 = time()
#     for _ in range(1000):
#         result = 0
#         for arr in make(1, 17):
#             result += number(arr)
#     t1 = time()
#     print(t1-t0)
