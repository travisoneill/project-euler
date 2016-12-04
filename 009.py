from math import sqrt

#ONE LINER
# problem9 = lambda n: [(a, int(sqrt(c**2 - a**2)), c) for a in range(1, int(0.3*n+1)) for c in range(int(0.4*n), int(0.5*n+1)) if abs(sqrt(c**2 - a**2) - int(sqrt(c**2 - a**2))) % 1 < 0.0001 and abs(a + sqrt(c**2 - a**2) + c - n) < 0.0001]

for c in range(415, 500):
    for a in range(1, 292):
        b = sqrt(c**2 - a**2)
        if abs(b - int(b)) % 1 < 0.0001 and abs(a + b + c - 1000) < 0.0001:
            print(a, b, c)
