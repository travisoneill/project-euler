from math import factorial
n = factorial(100)
digit_sum = 0
while n > 0:
    digit_sum += n % 10
    n //= 10
print(digit_sum)
