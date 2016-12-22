def closest(frac, limit):
    min_diff = -1
    n = None
    d = None
    for i in range(2, limit+1):
        if i*frac % 1 == 0: continue
        closest_numerator = int(i * frac)
        diff = closest_numerator/i - frac
        if diff > min_diff:
            min_diff = diff
            n, d = closest_numerator, i
    return (n, d)
