# from math import sqrt
from benchmark import benchmark
from simplemath import is_perfect_square, int_sqrt, square_root, int_log10
# from primesandfactors import prime_factors

def continued_frac_sqrt(n, p=None):
    '''returns array from of the repeating sequence of the continued fraction
    representation of the square root of n'''
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
                return continued_frac_sqrt(n, p*2)
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
            return array

def long_div(num, denom, prec):
    '''long division returning integer corresponding to the result with
    decimal removed at specified precision'''
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

def digit(num, d):
    '''get digit at index d in integer num'''
    shift = int_log10(num) - d + 1
    if shift > 0:
        return num % 10**shift // 10**(shift - 1)
    else:
        return 0

def frac(array):
    '''returns tuple (num, denom) simplified fraction for continued fraction in array format'''
    d, n = 1, array[-1]
    for x in reversed(array[:-1]):
        prev_n = n
        prev_d = d
        d = prev_n
        n = x * d + prev_d
    return (n, d)

def frac_expand_sqrt(n, limit=None):
    '''generates continued fraction series term for the square root of n'''
    f = continued_frac_sqrt(n)
    fraction = f[:1]
    repeating = f[1:]
    i = 0
    while True:
        yield frac(fraction)
        if limit and i > limit: break
        idx = i % len(repeating)
        fraction.append(repeating[idx])
        i += 1

is_dio = lambda x, y, d: x*x - d*y*y == 1

@benchmark()
def run(n):
    mx = (0,0)
    for d in range(n):
        if is_perfect_square(d): continue
        for fr in frac_expand_sqrt(d):
            if is_dio(*fr, d):
                if fr[1] > mx[1]:
                    mx = fr
                    print(d, fr)
                break
