from generators import primes

def greatest_phi_ratio_under(n):
    x = 1
    for p in primes(None):
        if x * p > n: break
        x *= p
    return x
