def run(n):
    i = 1
    tot = 0
    while True:
        x = (n // (4*i)) - i 
        if x <= 0:
            break
        tot += x
        i += 1
    return tot
