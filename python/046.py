cache = { 2: True }
def is_prime(n):
    if n < 2: return False
    if cache.get(n): return True
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1 + i%2
    cache[n] = True
    return True

def odd_composite():
    i = 3
    while True:
        if not is_prime(i): yield(i)
        i += 2

def goldbach(n):
    i = 1
    while 2*i**2 < n:
        diff = n - 2*i**2
        if is_prime(diff):
            return '{} + 2*{}^2'.format(diff, i)
        i += 1

def run():
    for c in odd_composite():
        if not goldbach(c):
            return c
