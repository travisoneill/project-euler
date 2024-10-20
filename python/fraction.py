import math
from simplemath import is_perfect_square, int_sqrt, int_log10

class Frac:
    def __init__(self, num, denom=1):
        self.numerator = num
        self.denominator = denom
        self.simplify()

    def __add__(self, frac):
        if type(frac) is int:
            frac = Frac(frac, 1)
        num = frac.numerator * self.denominator + self.numerator * frac.denominator
        denom = self.denominator * frac.denominator
        return Frac(num, denom)
    
    def __sub__(self, frac):
        return self + -frac

    def __mul__(self, frac):
        if type(frac) is int:
            return Frac(self.numerator * frac, self.denominator)
        return Frac(self.numerator * frac.numerator, self.denominator * frac.denominator)
    
    def __neg__(self):
        return Frac(self.numerator * -1, self.denominator)
    
    def __truediv__(self, frac):
        if type(frac) is int:
            frac = Frac(frac, 1)
        return self.__mul__(frac.inverse())
    
    def __pow__(self, exp):
        if type(exp) is not int:
            raise 'no float exp'
        out = Frac(self.numerator**abs(exp), self.denominator**abs(exp))
        return out.inverse() if exp < 0 else out
    
    def __float__(self):
        return self.numerator / self.denominator
    
    def __eq__(self, other):
        other.simplify()
        self.simplify()
        return self.denominator == other.denominator and self.numerator == other.numerator
        
    def inverse(self):
        return Frac(self.denominator, self.numerator)
    
    def sqrt(self):
        if not is_perfect_square(self.numerator) or not is_perfect_square(self.denominator):
            return self.inexact_sqrt()
        return Frac(int_sqrt(self.numerator), int_sqrt(self.denominator))
    
    def inexact_sqrt(self):
        num_root = int_sqrt(self.numerator)
        diff1, diff2 = abs(self.numerator - num_root**2), abs(self.numerator - (num_root+1)**2)
        new_num = num_root if diff1 < diff2 else num_root+1

        den_root = int_sqrt(self.denominator)
        diff1, diff2 = abs(self.denominator - den_root**2), abs(self.denominator - (den_root+1)**2)
        new_den = den_root if diff1 < diff2 else den_root+1
        return Frac(new_num, new_den)


    
    def simplify(self):
        gcd = math.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        if self.denominator < 0:
            self.denominator *= -1
            self.numerator *= -1

    def truncate(self, n):
        diff = min(int_log10(abs(self.numerator)), int_log10(abs(self.denominator))) - n
        if diff > 0:
            self.numerator //= 10**diff
            self.denominator //= 10**diff
        self.simplify()
    
    def __repr__(self):
        return f'{self.numerator}/{self.denominator}'