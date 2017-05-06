from itertools import permutations, combinations
from collections import Counter

from generators import primes2, miller_rabin_range
from primesandfactors import is_prime, prime_factors
from benchmark import benchmark


# @benchmark()
def split_prime(n: int):
    splits = set()
    if n % 10 in {4, 6, 8}:
        return splits
    def split_on_primes(before: tuple, n: int, after: tuple):
        if n < 10: return
        idx = 0
        left = 0
        lst = list(map(int, list(str(n))))
        while idx < len(lst):
            left *= 10
            left += lst[idx]
            right = join(lst[idx+1:])
            if is_prime(left):
                tup = []
                if left > 0:
                    tup.append(left)
                if right > 0:
                    tup.append(right)
                splits.add( before + tuple(tup) + after )
                if left and right:
                    if left > 0:
                        split_on_primes(before, left, (right,) + after)
                    if right > 0:
                        split_on_primes(before + (left,), right, after)
            idx += 1
        res = []
        for s in splits:
            if is_prime(s[-1]):
                res.append(s)
        return res

    return split_on_primes(tuple(), n, tuple())

def split_prime2(n: int):
    splits = set()
    if n % 10 in {4, 6, 8}:
        return splits
    if n % 10 in {2, 5} and n % 100 // 10 in {4, 6, 8}:
        return splits
    def split_on_primes(before: tuple, n: int, after: tuple):
        if n < 10: return
        idx = 0
        left = 0
        lst = list(map(int, list(str(n))))
        while idx < len(lst):
            left *= 10
            left += lst[idx]
            right = join(lst[idx+1:])
            if left in prime_set if left < 10000000 else is_prime(left):
                prime_set.add(left)
                tup = []
                if left > 0:
                    tup.append(left)
                if right > 0:
                    tup.append(right)
                splits.add( before + tuple(tup) + after )
                if left and right:
                    if left > 0:
                        split_on_primes(before, left, (right,) + after)
                    if right > 0:
                        split_on_primes(before + (left,), right, after)
            idx += 1
        res = []
        for s in splits:
            if s[-1] in prime_set:
                res.append(s)
        return res

    return split_on_primes(tuple(), n, tuple())


def split_on_primes(before: tuple, n: int, after: tuple):
    splits = set()
    if n < 10: return
    idx = 0
    left = 0
    lst = list(map(int, list(str(n))))
    while idx < len(lst):
        left *= 10
        left += lst[idx]
        right = join(lst[idx+1:])
        if left in prime_set:
            prime_set.add(left)
            tup = []
            if left > 0:
                tup.append(left)
            if right > 0:
                tup.append(right)
            splits.add( before + tuple(tup) + after )
            if left and right:
                if left > 0:
                    split_on_primes(before, left, (right,) + after)
                if right > 0:
                    split_on_primes(before + (left,), right, after)
        idx += 1
    res = []
    for s in splits:
        if s[-1] in prime_set:
            res.append(s)
    return res

def split_prime3(n: int):
    splits = set()
    if n % 10 in {4, 6, 8}:
        return splits
    if n % 10 in {2, 5} and n % 100 // 10 in {4, 6, 8}:
        return splits
    return split_on_primes(tuple(), n, tuple())


def handle_8(n: int):
    pass

def is_prime_tup(tup: tuple):
    if tup[-1] in {2, 4, 6, 8, 0, 5}:
        return False
    else:
        num = 0

def join(tup: tuple):
    num = 0
    for digit in tup:
        num *= 10
        num += digit
    return num


@benchmark()
def mr(n):
    [x for x in miller_rabin_range(n)]

@benchmark()
def pr(n):
    [x for x in primes2(n)]

# @benchmark()
def possible_primes(num_digits: int):
    primes = set()
    digits = [n for n in range(1, 10)]
    for c in combinations(digits, num_digits):
        if num_digits == 8 and 2 in c and 3 in c and 5 in c and 7 in c:
            continue
        for p in permutations(c):
            number = join(p)
            if is_prime(number):
                primes.add(number)
    return primes

@benchmark()
def all_primes(n):
    p = set()
    for i in range(1, n):
        p |= possible_primes(i)
        print(i)
    return p


def has_repeated_digits(n: int):
    return digit_counter(n).most_common(1)[0][1] > 1

#tested faster than repeated division
def digit_counter(n: int):
    return Counter(str(n))

@benchmark()
def test():
    for p in permutations([1,2,3,4,5,6,7,8,9]):
        join(p)

@benchmark()
def run():
    dig = [1,2,3,4,5,6,7,8,9]
    for p in permutations(dig):
        sp = split_prime(join(p))
        if sp:
            print(sp)

prime_set = set()
@benchmark()
def run2():
    global prime_set
    prime_set = all_primes(8)
    dig = [1,2,3,4,5,6,7,8,9]
    count = 0
    for p in permutations(dig):
        sp = split_prime2(join(p))
        if sp:
            count += len(sp)
            print(sp, count)
    return count

@benchmark()
def run3():
    global prime_set
    prime_set = all_primes(8)
    dig = [1,2,3,4,5,6,7,8,9]
    count = 0
    for p in permutations(dig):
        sp = split_prime3(join(p))
        if sp:
            count += len(sp)
            print(sp, count)
    return count

# def to_tup(n: int):
#     tup = []
#     while n > 0:


dc = digit_counter
pp = possible_primes
ap = all_primes
sop = split_prime
n0 = 254789631
n1 = 136987452




# 9
# 8 1
# 7 2
# 7 1 1
# 6 3
# 6 2 1
# 6 1 1 1
# 5 4
# 5 3 1
# 5 2 2
# 5 2 1 1
# 5 1 1 1 1
# 4 4 1
# 4 3 2
# 4 3 1 1
# 4 2 2 1
# 4 2 1 1 1
# 3 3 3
# 3 3 2 1
# 3 3 1 1 1
# 3 2 2 2
# 3 2 2 1 1
# 3 2 1 1 1 1
# 2 2 2 2 1
# 2 2 2 1 1 1
