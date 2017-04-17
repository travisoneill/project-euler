from math import sqrt, factorial
from itertools import combinations
from benchmark import benchmark

@benchmark()
def brute_force(n):
    count = 0
    for c in combinations(all_coords(n, n)[1:], 2):
        tri = origin_triangle(*c)
        if is_right(tri):
            count += 1
            # print(c)
    return count

def all_coords(x_range, y_range):
    return [ (x,y) for x in range(x_range+1) for y in range(y_range+1) ]

def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    a = x1 - x2
    b = y1 - y2
    return Root(a*a + b*b)

def origin_triangle(p1, p2):
    a = distance(p1, p2)
    b = distance((0,0), p1)
    c = distance((0,0), p2)
    return tuple(sorted((a,b,c)))

def is_right(triangle):
    a, b, c = triangle
    return a*a + b*b == c*c



class Root:
    def __init__(self, n_squared, coeff=1):
        self.root = n_squared
        self.coeff = coeff
        self.simplify()

    def simplify(self):
        i = 2
        while i * i <= self.root:
            if not self.root % (i*i):
                self.root //= i*i
                self.coeff *= i
            else:
                i += 1
        return self

    def __eq__(self, other):
        try:
            return other.root == self.root and self.coeff == other.coeff
        except:
            import pdb; pdb.set_trace()

    def __mul__(self, other):
        if other.__class__.__name__ == 'int':
            res = Root(self.root, self.coeff * other)
            return res
            # return int(res.coeff) if res.root == 1 else res
        elif other.__class__.__name__ == 'Root':
            res = Root(self.root * other.root, self.coeff * other.coeff)
            return res
            # return int(res.coeff) if res.root == 1 else res

    def __add__(self, other):
        if self.root != other.root:
            raise ValueError
        return Root(self.root, self.coeff + other.coeff)

    def __pow__(self, integer):
        res = Root(self.root**integer, self.coeff**integer)
        # return int(res.coeff) if res.root == 1 else res
        return res

    def __gt__(self, other):
        return float(self) > float(other)

    def __lt__(self, other):
        return float(self) < float(other)

    def __float__(self):
        return sqrt(self.root) * self.coeff

    def __repr__(self):
        rt = '' if self.root == 1 else '√{}'.format(self.root)
        co = '' if self.coeff == 1 else str(self.coeff)
        if not rt and not co:
            return str(self.coeff)
        else:
            return '{}{}'.format(co, rt)


def triangles_for(point, vector, limit):
    x, y = point
    dx, dy = vector
    points_to_right = min(y // dy, (limit - x) // dx)
    points_to_left = min((limit - y) // dy, x // dx)
    return points_to_left + points_to_right

def points_on(vector, limit):
    mult = 1
    while max(vector) * mult <= limit:
        v = (vector[0] * mult, vector[1] * mult)
        print(v, triangles_for(v, (vector[1], vector[0]), limit) )
        mult += 1


def triangles_for2(point, limit):
    x, y = point
    vector = tuple(reversed(simplify(point)))
    dx, dy = vector
    # print(min(y // dy, (limit - x) // dx))
    # print(min((limit - y) // dy, x // dx))
    return min(y // dy, (limit - x) // dx) + min((limit - y) // dy, x // dx)

def simplify(tup):
    i = 2
    while i <= min(tup):
        if not tup[0] % i and not tup[1] % i:
            tup = (tup[0] // i, tup[1] // i)
        else:
            i += 1
    return tup

@benchmark()
def run(limit):
    s = 0
    for x in range(1, limit+1):
        for y in range(1, limit+1):
            tup = (x, y)
            s += tf2(tup, limit)
    return s


p0 = (0,0)
p1 = (0,2)
p2 = (1, 1)

t0 = origin_triangle(p1, p2)
t1 = origin_triangle((1,0), (2,2))

bf = brute_force
d = distance
ot = origin_triangle
ir = is_right
ac = all_coords
tf = triangles_for
tf2 = triangles_for2
po = points_on
