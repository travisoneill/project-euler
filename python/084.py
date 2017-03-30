from random import randint
from collections import defaultdict

roll_dice = lambda d1, d2: randint(1, d1) + randint(1, d2)

def cc(n):
    r = randint(0, 15)
    if r == 0: return 0
    elif r == 1: return 10
    else: return n

def ch(n):
    r = randint(0, 15)
    if r == 0: return 0
    elif r == 1: return 10
    elif r == 2: return 11
    elif r == 3: return 24
    elif r == 4: return 39
    elif r == 5: return 5
    elif r == 6 or r == 7:
        if n == 7: return 15
        if n == 22: return 25
        if n == 36: return 5
    elif r == 8:
        if n == 22: return 28
        else: return 12
    elif r == 9: return n - 3
    else: return n

def run(n, d1, d2):
    d = defaultdict(lambda: 0)
    c_c = [2, 17, 33]
    c_h = [7, 22, 36]
    pos = 0
    for _ in range(n):
        d[pos] += 1
        pos = (pos + roll_dice(d1, d2)) % 40
        if pos in c_h: pos = ch(pos)
        if pos in c_c: pos = cc(pos)
        if pos == 30: pos = 10
    return d
