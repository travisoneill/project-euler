from math import log10
from benchmark import benchmark

@benchmark()
def run():
    count = 0
    for base in range(1, 10):
        exponent = 1
        while int(log10(base**exponent)) + 1 == exponent:
            count += 1
            # print(base, exponent, base**exponent)
            exponent += 1
    return count
