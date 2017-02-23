from benchmark import benchmark
from simplemath import is_perfect_square, int_log10, square_root, int_sqrt
from primesandfactors import prime_factors, is_prime

def frac_decompose(n, p=None):
    if is_perfect_square(n): return 0
    array = [ int_sqrt(n) ]
    p = p or int_sqrt(n) * 2 + 5
    s = square_root(n, p)
    br = int_sqrt(n) * 2 + 5
    while True:
        inc = 1
        i = 1
        while True:
            if i > br:
                return frac_decompose(n, p*2)
            array.append(i+inc)
            x = long_div(*frac(array), p)
            array.pop()
            array.append(i)
            y = long_div(*frac(array), p)
            if (s > x) ^ (s > y):
                if inc > 1:
                    inc = 1
                    array.pop()
                    continue
                else:
                    break
            array.pop()
            i += inc
            if i == 4 and inc == 1:
                inc = 10
        if array[-1] == array[0] * 2:
            return len(array) - 1

def digit(num, d):
    shift = int_log10(num) - d + 1
    if shift > 0:
        return num % 10**shift // 10**(shift - 1)
    else:
        return 0

def long_div(num, denom, prec):
    res = 0
    carry = digit(num, 0)
    dig = int_log10(num//denom)
    if dig > 0:
        prec += dig
    digits = 0
    count = False
    i = 1
    while True:
        res *= 10
        quot = carry // denom
        res += quot
        subtr = quot * denom
        carry = (carry - subtr) * 10 + digit(num, i)
        i += 1
        if quot: count = True
        if count: digits += 1
        if digits > prec: break
    return res

def frac(array):
    d, n = 1, array[-1]
    for x in reversed(array[:-1]):
        prev_n = n
        prev_d = d
        d = prev_n
        n = x * d + prev_d
    return (n, d)

@benchmark()
def run(n):
    odds = 0
    even_primes = set()
    for i in range(2, n):
        if is_prime(i):
            period = frac_decompose(i)
            if period % 2:
                odds += 1
            else:
                even_primes.add(i)
        else:
            if is_possibly_even_period(i, even_primes):
                x = frac_decompose(i)
                if x % 2:
                    odds += 1
    return odds

def is_possibly_even_period(n, evens):
    if is_perfect_square(n-1): return True
    prime_factors = set()
    divisor = 3
    while not n % 2:
        if 2 in prime_factors: return False
        prime_factors.add(2)
        n //= 2
    while divisor * divisor <= n:
        if not n % divisor:
            if divisor in evens: return False
            prime_factors.add(divisor)
            n //= divisor
        else:
            divisor += 2
    if n in evens: return False
    return True
