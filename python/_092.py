from benchmark import benchmark


def dig_square_sum(n: int):
    '''Returns the sum of the squares of the digits of n'''
    summ = 0
    while n > 0:
        dig = n % 10
        summ += dig*dig
        n //= 10
    return summ


def square_chain_89(n: int):
    '''Returns True if the square chain of n ends in a cycle with 89'''
    while True:
        if n == 89:
            return True
        if n == 1:
            return False
        n = dig_square_sum(n)


def get_test_set(n: int):
    '''Returns set of all the possibilites that end in 89 for an input n'''
    limit = 0
    while n > 0:
        limit += 81
        n //= 10
    s89 = set()
    for i in range(1, limit):
        if square_chain_89(i):
            s89.add(i)
    return s89


@benchmark()
def run(n: int):
    s89 = get_test_set(n)
    count = 0
    for i in range(1, n):
        if dig_square_sum(i) in s89:
            count += 1
    return count




from simplemath import int_log10
from itertools import combinations_with_replacement, permutations
from math import factorial

# def max_dig_sum(n: int):
#     max_sum = 0
#     while n > 0:
#         max_sum += 9
#         n //= 10
#     return max_sum

def c(n, r):
    return factorial(n) // (factorial(n-r) * factorial(r))

@benchmark()
def run2(n: int):
    '''only works for powers of 10'''
    count = 0
    s89 = get_test_set(n)
    digits = [d for d in range(1, 10)]
    num_digits = int_log10(n-1) + 1
    for d in range(1, num_digits+1):
        for comb in combinations_with_replacement(digits, d):
            sq_sum = sum([n*n for n in comb])
            if sq_sum in s89:
                possibilites = c(num_digits, d) * len({x for x in permutations(comb)})
                count += possibilites
    return count

from collections import Counter

@benchmark()
def run3(n: int):
    '''only works for powers of 10'''
    count = 0
    s89 = get_test_set(n)
    digits = [d for d in range(1, 10)]
    num_digits = int_log10(n-1) + 1
    for d in range(1, num_digits+1):
        for comb in combinations_with_replacement(digits, d):
            sq_sum = sum([n*n for n in comb])
            if sq_sum in s89:
                p = c(num_digits, d)
                #  * len({x for x in permutations(comb)})

                cc = [factorial(v) for k, v in Counter(comb).items()]
                f = factorial(d)
                for i in cc:
                    f //= i
                possibilites = p * f
                count += possibilites
    return count


from random import randint
def gen_random(type_selector):
    data_type = type_selector.split('[', 1)
    collection = '[]' in type_selector 

def analyzer(func):
    times = []
    for i in range(10)
