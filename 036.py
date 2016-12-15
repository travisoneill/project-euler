from math import log10

def is_palindrome(n):
    num_digits = int(log10(n)) + 1
    power = 0
    while power < num_digits // 2:
        n1 = (n // 10**power) % 10
        n2 = (n // 10**(num_digits - power - 1)) % 10
        if n1 != n2: return False
        power += 1
    return True

def to_binary(n):
    num_digits = int(log10(n)) + 1
    binary = 0
    power = 0
    while n > 0:
        binary += (n % 2)*10**power
        n //= 2
        power += 1
    return binary

def run(n):
    result = 0
    for i in range(1, n, 2):
        if is_palindrome(i) and is_palindrome(to_binary(i)):
            result += i
    print(result)
