from math import factorial
from time import time

def dig_fact(n):
    dig = []
    while n > 0:
        dig.append(n%10)
        n //= 10
    return sum(map(factorial, dig))

#DYNAMIC
loop_cache = {}
def loop_dynamic(n):
    count = 0
    x = n
    cache = {}
    while not cache.get(n):
        if loop_cache.get(n):
            count += loop_cache.get(n)
            break
        cache[n] = True
        n = dig_fact(n)
        count += 1
    loop_cache[x] = count
    return count

def run_dynamic(n):
    # [1 for x in range(n+1) if loop_dynamic(x) == 60]
    count = 0
    for n in range(n+1):
        if loop_dynamic(n) == 60:
            count += 1
    print(count)

def loop(n):
    count = 0
    cache = {}
    while not cache.get(n):
        cache[n] = True
        n = dig_fact(n)
        count += 1
    return count

def run(n):
    count = 0
    for n in range(n+1):
        if loop(n) == 60:
            count += 1
    print(count)

#RUN
run_dynamic(1000000)

#BENCHMARK
# def test(n):
#     t0 = time()
#     run(n)
#     t1 = time()
#     print(t1 - t0)
#     run_dynamic(n)
#     t2 = time()
#     print(t2 - t1)
