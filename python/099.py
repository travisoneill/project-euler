from math import log2
from benchmark import benchmark

@benchmark()
def run():
    max_value = 0
    max_line = 0
    line_number = 0
    with open('099.txt', 'r') as textfile:
        for line in textfile:
            line_number += 1
            base, exponent = map(int, line.strip().split(','))
            log2_result = log2(base) * exponent
            if log2_result > max_value:
                max_value = log2_result
                max_line = line_number
    print(max_line)
