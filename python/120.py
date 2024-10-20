def test(a, lim):
    for n in range(lim):
        s = (a-1)**n + (a+1)**n
        print(n, s % (a*a))


# (a - 1) ^ 2

# a^2 - 2a + 1
# a^2 + 2a + 1
# 2a^2 + 2

# a^3 - 3a^2 + 3a - 1
# a^3 + 3a^2 + 3a + 1
# 2a^3 + 6a

# a^4 - 4a^3 + 6a^2 - 4a + 1
# a^4 + 4a^3 + 6a^2 + 4a + 1
# a^4 + 12a^2 + 2

# a^5 - 5a^4 + 10a^3 - 10a^2 + 5a - 1
# a^5 + 5a^4 + 10a^3 + 10a^2 + 5a + 1
# 2a^5 + 20a^3 + 10a

# a * (2p % a)

# a*2 - a
# a^2 - 2a

def run(n):
    tot = 0
    for a in range(3, n+1):
        x = a*a - ((2-(a%2)) * a)
        tot += x
    print(tot)
        # print(a, x)
