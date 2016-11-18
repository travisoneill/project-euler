from math import sqrt

for c in range(415, 500):
    for a in range(1, 292):
        b = sqrt(c**2 - a**2)
        if abs(b - int(b)) % 1 < 0.0001 and abs(a + b + c - 1000) < 0.0001:
            print(a, b, c)
