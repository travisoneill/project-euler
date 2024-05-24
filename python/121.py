import math
from benchmark import benchmark

@benchmark()
def win_count(n):
    win_possibilities = 0
    for i in range(2**n):
        p = 1
        m = n
        wins = 0
        for _ in range(n):
            p *= ((i+1)%2) * (m-1) + 1
            wins += int(i%2)
            i >>= 1
            m -= 1
        
        win_possibilities += int(wins > n//2) * p
    prize = math.factorial(n+1) // win_possibilities
    print(prize)
