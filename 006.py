#ONE LINER
print(sum([n for n in range(101)]) ** 2 - sum([n**2 for n in range(101)]))

#FAST
def square_diff(n):
    s2 = (n**4 + 2 * n**3 + n**2) // 4
    s1 = n * (n + 1) * (2*n + 1) // 6
    print(s2 - s1)

square_diff(100)
