i = 2**31
mod = 10**10
n = 7830457 // 31
m = 7830457 % 31
x = 28433*2**m
for _ in range(n):
    x *= i
    x %= mod

print(x+1)
