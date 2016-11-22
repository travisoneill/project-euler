triangular = {}
pentagonal = {}
hexagonal = {}

t = lambda n: (n**2 + n) // 2
p = lambda n: (3*n**2 - n) // 2
h = lambda n: (2*n**2 - n)

n = 2
while True:
    triangular[t(n)] = True
    pentagonal[p(n)] = True
    hexagonal[h(n)] = True
    if hexagonal.get(t(n)) and pentagonal.get(t(n)):
        print(t(n))
    n += 1
