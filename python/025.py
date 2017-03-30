from stringmath import add_str
from functools import reduce

def first_fib_with_num_digits(n):
    a = '0'
    b = '1'
    idx = 1
    while len(b) < n:
        a, b = b, add_str(a, b)
        idx += 1
    return idx
