def int_sqrt(n):
    lo, hi = 1, n
    while hi - lo > 1:
        mid = (hi + lo) // 2
        val = mid * mid
        if val == n: return mid
        if val > n: hi = mid
        if val < n: lo = mid
    return lo
