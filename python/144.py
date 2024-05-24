
import math
from simplemath import is_perfect_square, int_sqrt, int_log10


def get_coeff(m, b, A, B):
    qa = B**2 + A**2 * m**2
    qb = m * A**2 * b * 2
    qc = A**2 * b**2 - A**2 * B**2
    return qa, qb, qc


def quad_solve(a, b, c):
    # -b +- sqrt(b^2 - 4ac) / 2a
    sq = b**2 - a*c*4
    root = sq.sqrt()
    r1 = (-b + root) / (a*2)
    r2 = (-b - root) / (a*2)
    return r1, r2


def elipse_intersect(m, b):
    A, B = Frac(5), Frac(10)
    coeff = get_coeff(m, b, A, B)
    return quad_solve(*coeff)

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


dot = lambda v1, v2: v1[0] * v2[0] + v1[1] * v2[1]
vec_mult = lambda vec, n: (vec[0] * n, vec[1] * n)
vec_sub = lambda vec1, vec2: (vec1[0] - vec2[0], vec1[1] - vec2[1])
tangent_slope = lambda x, y: (-x / y) * 4 


def reflect_vec(surface, incoming):
    normal = (surface[1], -surface[0])
    x = (dot(normal, incoming) / dot(normal, normal)) * 2
    return vec_sub(incoming, vec_mult(normal, x))


def get_y_intercept(point, slope):
    x, y = point
    return -x * slope + y


def reflect_line(incoming_slope, elipse_point):
    ex, ey = elipse_point
    slope = tangent_slope(ex, ey)
    reflect_surf = (Frac(1), slope)
    incoming_vec = (Frac(1), incoming_slope)
    reflected_vec = reflect_vec(reflect_surf, incoming_vec)
    
    ref_slope = reflected_vec[1] / reflected_vec[0]
    yint = get_y_intercept(elipse_point, ref_slope)
    return ref_slope, yint


def run():
    m, b = -Frac(197, 14), Frac(101,10)
    px, py = Frac(7,5), Frac(-48,5)

    i = 1
    while True:
        if (abs(float(px)) < 0.05 and abs(float(py) > 0)):
            print(i, float(px), float(py))
        i += 1
        if i > 500: break
        m, b = reflect_line(m, (px, py))
        x1, x2 = elipse_intersect(m,b)
        px = x1 if abs(float(x2) - float(px)) < 0.000001 else x2
        py = px * m + b
        if i > 10:
            px.truncate(50)
            py.truncate(50)
            m.truncate(50)
            b.truncate(50)

