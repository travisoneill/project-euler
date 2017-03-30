from math import sqrt

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def nth_prime(n):
    count = 2
    i = 3
    while count < n:
        i+=2
        if is_prime(i):
            count += 1
    print(i)

nth_prime(10001)
