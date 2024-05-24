def is_perfect_square(n):
    return int_sqrt(n) != int_sqrt(n-1)

def int_sqrt(n):
    if n < 2: return n
    lo, hi = 1, n
    while hi - lo > 1:
        mid = (hi + lo) // 2
        val = mid * mid
        if val == n: return mid
        if val > n: hi = mid
        if val < n: lo = mid
    return lo

def digital_sum(n):
    dig_sum = 0
    while n:
        dig_sum += n % 10
        n //= 10
    return dig_sum    


# def square_root(n, precision):
#     if n < 0: raise "Sorry, I don't do complex numbers!"
#     if n == 0: return 0
#     log_10 = -1
#     m = n
#     while n > 0:
#         log_10 += 1
#         n //= 10
#     exponent = 2 * (precision - log_10 // 2 ) - 2
#     return int_sqrt(m * 10**exponent)

def square_root(n, p):
    l = int_log10(n) // 2 + 1
    exponent = 2 * (p)
    val = int_sqrt(n * 10**exponent)
    return val

def int_log10(n):
    count = 0
    while n:
        count += 1
        n //= 10
    return count - 1
