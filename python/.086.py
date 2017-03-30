from math import sqrt, factorial
from itertools import combinations
from simplemath import is_perfect_square, int_sqrt

c = lambda n, r: factorial(n) // ( factorial(r) * factorial(n-r) )
is_triple = lambda a, b: is_perfect_square(a**2 + b**2)

def euclid(m, n):
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    return (a, b, c)

def euclid_gen(max_legs):
    limit = int_sqrt(max_legs // 2) + 1
    for i in range(1, limit):
        for j in range(i+1, limit):
            yield euclid(j, i)

def run(m):
    total = 0
    for triple in euclid_gen(3*m):
        total += score(sorted(triple), m)
    return total
# 4x^2 > 3*lim
# x^2 == 1.5*lim
# x = sqrt(1.5*lim)

def l(n):
    return int_sqrt(n) + 1

def test(n):
    nums = tuple(range(1, n+1))
    count = 0
    for c in combinations(nums, 3):
        s = sorted(c)
        a = s[2]
        b = s[0] + s[1]
        if is_triple(a, b):
            print(c)
            count += 1
    for c in combinations(nums, 2):
        a = max(c)
        b = sum(c)
        a2 = 2*min(c)
        if is_triple(a, b):
            print(c)
            count += 1
        if is_triple(a, a2):
            print(c)
            count += 1
    return count


def score(triple, m):
    a, b, c = triple
    if  a > m or b > 2*m or a+b > 3*m:
        return 0
    s = 0
    s += max(a - b // 2, 0) + (not b % 2)
    if b <= m:
        s += a // 2
    return s

# 10 - 12
#
# def run(n):
#     total = 0
#     for t in get_triples(n):
#         total += score(t, n)
#     print(total)

# 8 15
#
# 8 7 8
#
# 15 7 1
# 15 6 2
# 15 5 3
# 15 4 4
#
# 1 7 15
# 2 6 15
# 3 5 15
# 4 4 15
#
#
# 20 21 29
#
# 20 20 1
# 20 19 2
# 20 18 3
# 20 17 4
# 20 16 5
# 20 15 6
# 20 14 7
# 20 13 8
# 20 12 9
# 20 11 10
#
# 21 19 1
# 21 18 2
# 21 17 3
# 21 16 4
# 21 15 5
# 21 14 6
# 21 13 7
# 21 12 8
# 21 11 9
# 21 10 10
#
# 10 24
#
# 10 12 12
#
# 24 9 1
# 24 8 2
# 24 7 3
# 24 6 4
# 24 5 5
#
#
# 15 20
#
# 15 10 10
# 15 11 9
# 15 12 8
# 15 13 7
# 15 14 6
# 15 15 5
#
# 20 14 1
# 20 13 2
# 20 12 3
# 20 11 4
# 20 10 5
# 20 9 6
# # 20 8 7
#
#
# 6 8
#
# 6 4 4
# 6 5 3
# 6 6 2
#
# a - b//2 = 2
#
# 9 12
#
# 9 6 6
# 9 7 5
# 9 8 4
# 9 9 3
#
# a - b // 2 = 3
#
# 8 15
#
# 24 45
# 24 23 22
# 24 24 21
#
# a - b //2 = 2

#
# 3 4
#
# 3 2 2
# 3 3 1
#
# 4 2 1
