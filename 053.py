from math import factorial
from benchmark import benchmark

combinations = lambda n, c: factorial(n) // ( factorial(n-c) * factorial(c) )

def number_over(row, limit):
    for i in range(row//2 + 1):
        if combinations(row, i) > limit:
            return row + 1 - 2 * i
    else:
        return 0

@benchmark()
def run(rows, limit):
    summ = 0
    for row in reversed(range(rows+1)):
        x = number_over(row, limit)
        if not x:
            return summ
        else:
            summ += x
