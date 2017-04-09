from benchmark import benchmark

def dig_square_sum(n: int):
    '''Returns the sum of the squares of the digits of n'''
    summ = 0
    while n > 0:
        dig = n % 10
        summ += dig**2
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
    s_89 = set()
    for i in range(1, limit):
        if square_chain_89(i):
            s_89.add(i)
    return s_89


@benchmark()
def run(n: int):
    s89 = get_test_set(n)
    count = 0
    for i in range(1, n):
        if dig_square_sum(i) in s89:
            count += 1
    return count
