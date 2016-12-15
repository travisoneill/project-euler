from math import factorial

def factorial_digit_sum(n):
    factorial_sum = 0
    while n > 0:
        factorial_sum += factorial(n%10)
        n //= 10
    return factorial_sum

result = 0
for n in range(3, factorial(9)*6):
    if n == factorial_digit_sum(n):
        result += n
print(result)
