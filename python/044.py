from math import sqrt

pentagonal = lambda n: (3*n**2 - n) // 2
inverse_pentagonal = lambda n: (sqrt(24*n+1)+1) / 6
is_pentagonal = lambda n: inverse_pentagonal(n) % 1 == 0

def search(limit, interval=1):
    pent = [ pentagonal(n) for n in range(1, limit) ]
    while interval < len(pent):
        if interval == len(pent): return False
        for i in range(len(pent)-interval):
            a, b = pent[i], pent[i+interval]
            if is_pentagonal(a+b) and is_pentagonal(b-a):
                print((a, b))
        interval += 1
