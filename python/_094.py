from math import sqrt
from benchmark import benchmark
from simplemath import is_perfect_square

def heron_area_squared(a, b, c):
    p = (a + b + c) // 2
    return p * (p - a) * (p - b) * (p - c)

def heron2(a, b, c):
    p = (a + b + c) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))
#
# p^2 -pa (p - b)
# p^3 -p^2a -p^2b + pab (p - c)
# p^4 -p^3a -p^3b + p^2ab -p^3c +p^2ac +p^2bc -pabc
#
# p * p^3 -(2p)p^3 + (ab +ac +bc)p^2 -(abc)p

def analyze(a, b, c):
    p = (a + b + c) // 2
    print(p, p**2, p**3)
    print(a + b +c)
    print(a*b + a*c + a*b)
    print(a * b * c)

@benchmark()
def test2(limit):
    for a in range(2, limit):
        if not a % 2:
            h1 = heron2(a, a+1, a+1)
            if h1 % 1 == 0:
                print(a, a+1, a+1)
        else:
            h2 = heron2(a, a, a+1)
            if h2 % 1 == 0:
                print(a, a, a+1)
        # is_perfect_square(int(h1))
        # is_perfect_square(int(h2))
        # sqrt(h1)
        # sqrt(h2)




@benchmark()
def test(limit):
    a = 1
    while a < limit:
        if a % 2 == 0:
            h1 = heron_area_squared(a, a+1, a+1)
            if is_perfect_square(h1):
                print(a, a+1, a+1, h1, (3*a+2)/2)
        else:
            h2 = heron_area_squared(a, a, a+1)
            if is_perfect_square(h2):
                print(a, a, a+1, h2, (3*a+1)/2)
        a += 1

@benchmark()
def test3(limit):
    matches = [16]
    test = 15
    interval = 1
    direction = 1
    ratio = 3
    while matches[-1] < limit:
        if test % 2 == 0:
            h1 = heron_area_squared(test, test+1, test+1)
            if is_perfect_square(h1):
                perimeter = test + test+1 + test+1
                ratio = perimeter / matches[-1]
                matches.append(perimeter)
                test = int(test * ratio)
                interval = 1
                continue
        else:
            h2 = heron_area_squared(test, test, test+1)
            if is_perfect_square(h2):
                perimeter = test + test + test+1
                # ratio = perimeter / matches[-1]
                matches.append(perimeter)
                test = int(test * ratio)
                interval = 1
                continue
        test += interval * direction
        interval += 1
        direction *= -1
    return sum(matches[:-1])

def area(s1, s2, s3):
    c = s2
    a = s3 // 2 if s1 == s2 else s1 // 2
    b  = sqrt(c*c - a*a)
    return b * a



@benchmark()
def test4(limit):
    matches = [16]
    side1 = 6
    direction = 1
    ratio = 2 + sqrt(3)
    while matches[-1] < limit:
        side2 = side1 if side1 % 2 == 1 else side1 + 1
        area_squared = heron_area_squared(side1, side2, side1 + 1)
        print(area_squared)
        if is_perfect_square(area_squared):
            perimeter = side1 + side2 + side1 + 1
            matches.append(perimeter)
            side1 = int(side1 * ratio)
            direction *= -1
            continue
        side1 += direction
    return sum(matches[:-1])
