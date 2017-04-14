from generators import fibonacci2
from benchmark import benchmark

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
            while first9 > 1000000000:
                first9 //= 10
            print(idx, first9)
            if is_pandigital(first9):
                print(fib)
                break

def fib_mod(mod):
    a, b = 0, 1
    while True:
        yield b
        a, b = b, (a + b) % mod

def run2():
    idx = 0
    for fib in fib_mod(1000000000):
        idx += 1
        if is_pandigital(fib):
            print(idx, fib)
            # first9 = fib
            # while first9 > 1000000000:
            #     first9 //= 10
            # if is_pandigital(first9):
                # print(fib)
                # break
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
            i = i1 * i2 + c1 * c2 * root * root
            c = i1 * c2 + i2 * c1
            d = d1 * d2
            return Root(self.root, i, c, d)

    def __flt__():


    def __pow__(self, exp):
        pass

    def __str__(self):
        operator = '+' if self.coefficient > 0 else '-'
        coeff = abs(self.coefficient) or 0
        coeff = '' if coeff == 1 else coeff
        numerator = '{} {} {}√{}'.format(self.integer, operator, coeff, self.root)
        line = '-' * len(numerator)
        denom = ' ' * ((len(numerator) - 1) // 2) + str(self.divisor)
        if self.divisor == 1:
            return numerator
        else:
            return '\n'.join([numerator, line, denom])


r5 = Root(5, -1, 1, 2)
print(r5)

def poly_power(poly, exp):
    pass
