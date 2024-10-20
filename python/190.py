def max_prod(n):
    base = 2 / (n+1)
    prod = 1
    for i in range(1, n+1):
        prod *= (base * i)**i
    return prod

def run(n1, n2):
    tot = 0
    for i in range(n1, n2+1):
        tot += int(max_prod(i))
    return tot
