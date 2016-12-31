from benchmark import benchmark

def square_root(n, precision):
    if n < 0: raise 'No sqrt for negative numbers'
    if n == 0: return 0
    log_10 = -1
    m = n
    while n > 0:
        log_10 += 1
        n //= 10
    exponent = 2 * (precision - log_10 // 2 ) - 2
    return int_sqrt(m * 10**exponent)

def int_sqrt(n):
    lo, hi = 1, n
    while hi - lo > 1:
        mid = (hi + lo) // 2
        val = mid * mid
        if val == n: return mid
        if val > n: hi = mid
        if val < n: lo = mid
    return lo

def digital_sum(n):
    d_sum = 0
    while n > 0:
        d_sum += n % 10;
        n //= 10;
    return d_sum

@benchmark()
def run(n, precision):
    total = 0
    for i in range(n+1):
        x = int_sqrt(i)
        if x * x == i: continue
        total += digital_sum(square_root(i, precision))
    print(total)

#TODO take str multiplier from old approch and adapt for module
#
# from stringmath import add_str
# from math import sqrt
# from functools import reduce

# def squared_decimal(string):
#     if string >= '0.0001': return mult_str(string, string)
#     decimal = string.split('.')[-1]
#     trimmed = decimal.lstrip('0')
#     leading_zeroes = '0' * (2 * ( len(decimal) - len(trimmed) ))
#     trimmed = '0.' + trimmed
#     result = mult_str(trimmed, trimmed)
#     return '0.' + leading_zeroes + result.split('.')[-1]
#
# def run(n):
#     res = 0
#     for i in range(1, n+1):
#         res += root(i, 100)
#         print(res)
#     return res
#
# def root(n, decimal_precision):
#     if sqrt(n) % 1 == 0: return 0
#     square_root = str(sqrt(n))[:-2] #issue if n > 10^12
#     decimals = len(square_root.replace('.', ''))
#     zeroes = '0' * len(square_root.split('.')[-1])
#     digital_sum = reduce( lambda x, y: x + int(y), square_root.replace('.', ''), 0 )
#     last = mult_str(square_root, square_root)
#     test_val = last
#     while decimals < decimal_precision:
#         for digit in range(1, 10):
#             store = test_val
#             ab = '0.' + str(digit)
#             a1 = mult_str(ab, '2')
#             a2 = mult_str(a1, square_root)
#             a = '0.' + add_str(zeroes, a2.split('.')[0]) + a2.split('.')[-1] if zeroes else a2
#
#             b = squared_decimal( '0.' + zeroes + str(digit) )
#             c = add_str(a, b)
#             test_val = add_str(last, c)
#             if int(test_val.split('.')[0]) >= n:
#                 square_root += str(digit-1)
#                 last = store
#                 test_val = store
#                 break
#         else:
#             square_root += str(digit)
#             last = test_val
#
#         zeroes += '0'
#         decimals += 1
#         digital_sum += int(square_root[-1])
#     return digital_sum
#
# def mult_str(*args):
#     return reduce(multiplier, args)
#
# def multiplier(x, y):
#     if len(x) < len(y): x, y = y, x
#     negative = '-' if (x[0] == '-') ^ (y[0] == '-') else ''
#     carry = 0
#     if x[-1] == '.': x += '0'
#     if y[-1] == '.': y += '0'
#     x_decimal = len(x) - x.index('.') - 1 if '.' in x else 0
#     y_decimal = len(y) - y.index('.') - 1 if '.' in y else 0
#     result = '0'
#     zeroes = ''
#     carry = 0
#     for dx in reversed(x):
#         if dx == '.' or dx == '-': continue
#         num = zeroes[:]
#         for dy in reversed(y):
#             if dy == '.' or dy == '-': continue
#             sm = int(dx) * int(dy) + carry
#             digit = sm % 10
#             num = str(digit) + num
#             carry = sm // 10
#         if carry > 0: num = str(carry) + num
#         carry = 0
#         zeroes += '0'
#         result = add_str(result, num)
#
#     if x_decimal or y_decimal:
#         decimal_place = len(result) - x_decimal - y_decimal
#         result = negative + result[:decimal_place] + '.' + result[decimal_place:]
#     else:
#         result = negative + result
#
#     return process(result)
#
# def process(string):
#     negative = '-' if string[0] == '-' else ''
#     string = string[1:] if negative else string
#     string = string.lstrip('0')
#     if not string: return '0'
#     if '.' in string: string = string.rstrip('0')
#     if string == '.': return '0.0'
#     if string[0] == '.': string = '0' + string
#     if string[-1] == '.': string += '0'
#     return negative + string
