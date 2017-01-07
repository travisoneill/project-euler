from operator import mul
from functools import reduce
from benchmark import benchmark

triangular = lambda n: (n**2 + n) // 2

def to_base(n, base):
    num = []
    while n > 0:
        num.append(n % base)
        n //= base
    num.reverse()
    return num

def run(x, prime_base=7):
    digit_array = to_base(x, prime_base)
    term_base = triangular(prime_base)
    max_exponent = len(digit_array) - 1
    total = 0
    for i in range(len(digit_array)):
        coefficient = triangular(digit_array[i]) * reduce(mul, map(lambda n: n+1, digit_array[:i]), 1)
        total += coefficient * term_base**(max_exponent - i)
    print(total)

# def pascal(num_rows, base, flag=True):
#     row = [0, 1, 0]
#     count = 0
#     total = 0
#     results = []
#     adder = lambda n: False if n % base else True
#     display = lambda n: '0' if n % base else '1'
#     while count < num_rows:
#         s = sum(map(adder, row[1:-1]))
#         total += count - s + 1
#         # print(count, count % 7, s, count-s)
#         if flag: print( ''.join(list(map(display, row[1:-1]))) )
#         # else: print(count, count % 7, s, count-s+1)
#         else:
#             if count % 7 == 0:
#                 pass
#                 # if count % 49 == 0: print('')
#                 # print(count, count % 7, count % 49, count-s+1)
#         # if count % 7 == 6: print('')
#         next_row = [0]
#         for i in range(len(row)-1):
#             next_row.append(row[i] + row[i+1])
#         next_row.append(0)
#         row = next_row
#         count += 1
#     return total
