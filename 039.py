from math import sqrt

triples_of_perimeter = lambda n: { (a, int(sqrt(c**2 - a**2)), c) for a in range(1, 1 + (n * 3) // 10) for c in range((n * 4) // 10, (n * 5) // 10) if sqrt(c**2 - a**2) % 1 == 0 and a + sqrt(c**2 - a**2) + c == n }

mx = 0
max_triples = 0
for n in range(0, 1000, 2):
    if len(triples_of_perimeter(n)) > mx:
        mx = len(p)
        max_triples = n

print(max_triples)
