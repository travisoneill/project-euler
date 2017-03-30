from itertools import combinations
from benchmark import benchmark


def check(n, die1, die2):
    '''Checks if 2 digit number n can be formed by 2 dice'''
    d2 = n % 10
    d1 = n // 10
    if d2 in die2 and d1 in die1:
        return True
    if d1 in die2 and d2 in die1:
        return True
    return False


def check_squares(die1, die2):
    '''Returns true if all 2 digit squares can be formed by two dice'''
    for n in (0, 1, 2, 3, 4, 5, 6, 8):
        if n not in die1 and n not in die2:
            return False
    for i in (1, 4, 9, 16, 25, 36, 49, 64, 81):
        if not check(i, die1, die2):
            return False
    return True


def add_6_or_9(sett):
    '''If set contains 6 or 9 return set containing 6 and 9'''
    if 6 in sett:
        sett.add(9)
    if 9 in sett:
        sett.add(6)
    return sett


def mapper(tup):
    return add_6_or_9(set(tup))

def all_dice(n):
    '''Returns list of all possible dice with n faces and single digit values'''
    digits = set(range(10))
    dice = list(map(mapper, combinations(digits, n)))
    return dice


@benchmark()
def run():
    '''iterate over all possible dice pairs and increment count if all
    two digit squares can be formed'''
    count = 0
    dice = all_dice(6)
    for i in range(len(dice)):
        for j in range(i, len(dice)):
            if check_squares(dice[i], dice[j]):
                count += 1
    return count
