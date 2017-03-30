from math import sqrt

def simplify(frac):
    num = frac[0]
    denom = frac[1]
    i = 2
    while i <= sqrt(denom):
        if num % i == 0 and denom % i == 0:
            num /= i
            denom /= i
            continue
        i += 1
    return (num, denom)

def process(frac, digits):
    n = frac[0]
    d = frac[1]
    for i in range(1, 10**digits // d):
        n10 = n * i // 10
        n1 = n * i % 10
        d10 = d * i // 10
        d1 = d * i % 10
        f = (n10, n1, d10, d1)
        if min(f) == 0:
            continue
        if check(f):
            print((n10, n1, d10, d1))
            return (n10, n1, d10, d1)

def check(frac):
    n = frac[0] * 10 + frac[1]
    d = frac[2] * 10 + frac[3]
    q = n / d
    if frac[1] == frac[2]:
        return float_eq(q, frac[0] / frac[3])
    elif frac[0] == frac[3]:
        return float_eq(q, frac[0] / frac[3])


def float_eq(n1, n2):
    return abs(n1 - n2) < 0.000001

numerator = 1
denominator = 1
for d in range(2, 10):
    for n in range(1, d):
        f = (n, d)
        if f != simplify(f):
            continue
        frac = process(f, 2)
        if frac:
            numerator *= (frac[0] * 10 + frac[1])
            denominator *= (frac[2] * 10 + frac[3])

print(simplify((numerator, denominator)))
