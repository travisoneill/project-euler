import sys
from benchmark import benchmark

def all_splits(n):
    pow = 1
    while n > pow:
       yield n // pow, n % pow
       pow *= 10


def all_partitions(n, root):
    if n < 10:
        yield [n]
    for first, rest in all_splits(n):
        for p in all_partitions(rest):
            if first + sum(p) >= root:                
                yield [first] + p

def dig_sum(n):
    s = 0
    while n > 0:
        s += n%10
        n //= 10
    return s


def dsum(n):
    while n > 9:
        n = dig_sum(n)
    return n

@benchmark()
def main(limit):
    tot = 0
    counted, found = 0, 0
    for n in range(2, limit+1):
        if dsum(n) not in (1, 9):
            continue
        sq = n*n
        counted += 1
        for p in all_partitions(sq):
            if sum(p) == n:
                print(n, sq, p)
                tot += sq
                found += 1
                break
    print(f'counted: {counted}, found: {found}')
    return tot

if __name__ == '__main__':
    tot = main(int(sys.argv[1]))
    print(tot)
