from generators import fibonacci2
from benchmark import benchmark
from simplemath import int_log10

def is_pandigital(n):
    digits = set([0])
    while n > 0:
        digits.add(n % 10)
        n //= 10
    return len(digits) == 10

ip = is_pandigital

def run():
    idx = 0
    for fib in fibonacci2():
        idx += 1
        if is_pandigital(fib % 1000000000):
            first9 = fib
            digits = int_log10(first9) + 1
            first9 //= 10**(digits - 9)
            print(idx, first9)
            if is_pandigital(first9):
                return idx

def fib_mod(mod):
    a, b = 0, 1
    while True:
        yield b
        a, b = b, (a + b) % mod

@benchmark()
def run2():
    idx = 0
    for fibo in fib_mod(1000000000):
        idx += 1
        if is_pandigital(fibo):
            print(idx, fibo)
            full_number = fib(idx)
            if is_pandigital(int(full_number[:9])):
                print(idx, full_number[:9])
                break

@benchmark()
def run3():
    idx = 0
    for fibonacci in fib_mod(1000000000):
        idx += 1
        if is_pandigital(fibonacci):
            print(idx, fibonacci)
            full_number = fibo(idx)
            if is_pandigital(int(full_number[:9])):
                print(idx, full_number[:9])
                break

@benchmark()
def run4():
    idx = 0
    for fibonacci in fib_mod(1000000000):
        idx += 1
        if is_pandigital(fibonacci):
            print(idx, fibonacci)
            full_number = fibo3(idx)
            if is_pandigital(int(full_number[:9])):
                print(idx, full_number[:9])
                break

from math import sqrt
def fibonacci_at_index(idx):
    pass

def t(n):
    x = (1 + sqrt(5)) / 2
    y = (1 - sqrt(5)) / 2
    print(y**n)
    print(x**n)
    print((x**n - y**n) * (1 / sqrt(5)))
    print((x**n) * (1 / sqrt(5)))

# 1 + r5         1 - r5
#
# 1 + 3*1*r5 + 3*1*5 + 5r5
# 16 + 8r5
#                 6 - 2r5
#                 10 -6r5    10
# # 1 + 2r5 + 1
# # r5 + 10 + r5
# 2r5 + 16

# class Root:
#     def __init__(self, squared):
#         self.squared = squared
#
#     def __pow__(self, exp):
#         return self.squared**(exp // 2)
#
#     def __str__(self):
#         return '√{}'.format(self.squared)

from primesandfactors import least_common_mult
class Root:
    def __init__(self, root, integer=0, coefficient=1, divisor=1):
        from math import sqrt
        self.integer = integer
        self.root = root
        self.coefficient = coefficient
        self.divisor = divisor

    def __mul__(self, other):
        if other.__class__.__name__ == 'int':
            coeff = self.coefficient * other
            integer = self.integer * other
            return Root(self.root, integer, coeff, self.divisor)
        if other.__class__.__name__ == 'Root':
            if self.root != other.root:
                raise ValueError
            c1, c2 = self.coefficient, other.coefficient
            i1, i2 = self.integer, other.integer
            d1, d2 = self.divisor, other.divisor
            root = self.root
            i = i1 * i2 + c1 * c2 * root
            c = i1 * c2 + i2 * c1
            d = d1 * d2
            return Root(self.root, i, c, d)

    def __pow__(self, integer):
        if integer == 0:
            return 1
        bits = []
        while integer > 0:
            bits.append(integer%2)
            integer //= 2
        mult = Root(self.root, self.integer, self.coefficient, self.divisor)
        mults = [mult]
        while len(mults) < len(bits):
            nxt = mults[-1] * mults[-1]
            mults.append(nxt)
        res = Root(self.root, 1, 0, 1)
        for idx, bit in enumerate(bits):
            if bit == 1:
                # print(mults[idx])
                res *= mults[idx]
        return res
        # for _ in range(integer - 1):
            # res *= mult
        # print(bits)
        # return mults

    def __float__(self):
        return (self.integer + self.coefficient * sqrt(self.root)) / self.divisor

    def __add__(self, other):
        if self.root != other.root:
            raise ValueError
        c1, c2 = self.coefficient, other.coefficient
        i1, i2 = self.integer, other.integer
        d1, d2 = self.divisor, other.divisor
        lcm = least_common_mult(d1, d2)
        m1, m2 = lcm // d1, lcm // d2
        i = i1 * m1 + i2 * m2
        c = c1 * m1 + c2 * m2
        return Root(self.root, i, c, lcm)

    def __sub__(self, other):
        if self.root != other.root:
            raise ValueError
        c1, c2 = self.coefficient, other.coefficient
        i1, i2 = self.integer, other.integer
        d1, d2 = self.divisor, other.divisor
        lcm = least_common_mult(d1, d2)
        m1, m2 = lcm // d1, lcm // d2
        i = i1 * m1 - i2 * m2
        c = c1 * m1 - c2 * m2
        return Root(self.root, i, c, lcm)

    def __repr__(self):
        operator = '+' if self.coefficient > 0 else '-'
        coeff = abs(self.coefficient) or 0
        coeff = '' if coeff == 1 else coeff
        numerator = '{} {} {}√{}'.format(self.integer, operator, coeff, self.root)
        line = '-' * len(numerator)
        denom = ' ' * ((len(numerator) - 1) // 2) + str(self.divisor)
        if self.divisor == 1:
            return numerator
        else:
            return '\n'.join([numerator, line, denom]) + '\n'


r1 = Root(5, 1, -1, 2)
r2 = Root(5, 1, 1, 2)
r3 = Root(5, 0, 1, 5)
a = (1 + sqrt(5)) / 2
b = (1 - sqrt(5)) / 2
c = 1 / sqrt(5)
def fibo(n):
    x = (r2**n - r1**n) * r3
    return str(x.integer // x.divisor)

def fibo2(n):
    x = (r2**n) * r3
    return str(x.integer // x.divisor)

def poly_power(poly, exp):
    pass

def identity_matrix(n):
    """Returns the n by n identity matrix."""
    r = list(range(n))
    return [[1 if i == j else 0 for i in r] for j in r]

def fib2(N):
    if N == 0: return (0, 1)
    half_N, is_N_odd = divmod(N, 2)
    f_n, f_n_plus_1 = fib2(half_N)
    f_n_squared = f_n * f_n
    f_n_plus_1_squared = f_n_plus_1 * f_n_plus_1
    f_2n = 2 * f_n * f_n_plus_1 - f_n_squared
    f_2n_plus_1 = f_n_squared + f_n_plus_1_squared
    if is_N_odd:
        return (f_2n_plus_1, f_2n + f_2n_plus_1)
    return (f_2n, f_2n_plus_1)

def fib(N):
    return str(fib2(N)[0])


def fibo3(n):
    r = Root(5, 1, 1, 2)
    f = r ** n
    return str(2 * f.coefficient // f.divisor)
