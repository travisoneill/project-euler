# (1, 2i)

# 1 + 2i * 1 - 2i
# 1  - (2i)^2
# 1 + 4 = 5

# 2 + 2i * 3 - 3i
# 6 +6i -

# (2, -3), (2, 3)

# 1 + i, 1 - i
# 1 - i^2 = 2

class Complex:
    def __init__(self, rat=0, imag=0):
        self.rat = rat
        self.imag = imag

    def __mul__(self, other):
        if type(other) is int:
            return Complex(self.rat * other, self.imag * other)
        r = self.rat * other.rat
        ri = (self.imag * other.rat) + (self.rat * other.imag)
        i = -(self.imag * other.imag)
        return Complex(r+i, ri)

    def __add__(self, other):
        return Complex(self.rat + other.rat, self.imag + other.imag)
    
    def __repr__(self):
        if self.imag == 0:
            return str(self.rat)
        elif self.rat == 0:
            return f'{self.imag}i'
        else:
            sign = '+' if self.imag > 0 else '-'
            coeff = abs(self.imag) if abs(self.imag) > 1 else ''
            return f'{self.rat} {sign} {coeff}i'
        

c1 = Complex(1, 1)
c2 = Complex(1, -1)
    


# 1 + i, 2 - 2i
# 2  -2i^2 = 4

# 1+i, 4-4i
# 4 - 4i^2

# 1,2,4
# 1,2,4,8

# 4 2 1 (1, 2)

# (3 +2i) * (3 -2i)
# 9 + 4 = 13

# (3 + 4i), (3 - 4i)

# 1.5 1.5 

# 1,2 - 3
# 1,3 - 4
# 1,5 - 6

# 1,2,3,6 - 12
# 1,2,5,10 - 18
# 1,3,5,15 - 24

# 1,2,3,5,6,10,15,30 - 72

# 1,2,4 - 7
# 1,3,9 - 13
# 1,5,25 - 31

# 1,2,4,8 = 15
# 1,3,9,27 = 40
# 1,5,25,125 = 156


# 6)
# 1,2,3 (1+i), (1-i) (3+3i) (3-3i) 6
# 20


# 2/3 ^ 3 = 8/27

# 1/3*2/3*2/3 = 4/27 * 3 = 12/27

# 1/3*1/3*2/3 = 2/27 * 3 = 6/2


# 2/3^30 
# 1073741824
# 2^29 * 30

# .1 * 1.9^2 = 

# t = lambda n,m: n*(m**2)

# 2-x * x^2

# 2x^2 - x^3

# 4x - 3x^2 = 0
# 4 - 3x = 0
# 4 = 3x
# x = 4/3

# a * b^2 * c^3

# a + b + c = 3

# a = 3 - b - c


# 3-x * x^3

# 3x^3 - x^4

# 9x^2 - 4x^3 = 0
# 9 - 4x = 0
# 9 = 4x
# x = 9/4

# 3/4, 9/4

# 1/4, 1/2, 9/4

# 1/16 * 729/64

# a**2 * b**3
