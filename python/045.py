from math import sqrt

# ONE LINER
solve = lambda: [2*n*n - n for n in range(144, 100000) if sqrt(48*n**2 - 24*n + 1) % 6 == 5][0]


# hexagonal always triangular
# triangular = lambda n: (n**2 + n) // 2
pentagonal = lambda n: (3*n**2 - n) // 2
hexagonal = lambda n: (2*n**2 - n)

# inverse_triangular = lambda n: (sqrt(8*n+1)-1) / 2
inverse_pentagonal = lambda n: (sqrt(24*n+1)+1) / 6
inverse_hexagonal = lambda n: (sqrt(8*n+1)+1) / 4

def p_and_h_number(n):
    matches = 0
    n = 1
    while matches < 3:
        if(inverse_pentagonal(hexagonal(n)) % 1 == 0): matches += 1
        n += 1
    print(hexagonal(n))
