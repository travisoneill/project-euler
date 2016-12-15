from euler_utils_primesandfactors import is_prime

def run():
    primes = {}
    def primetest(n):
        if n in primes:
            return primes[n]
        else:
            primes[n] = is_prime(n)
            return primes[n]

    def is_truncatable_prime(n):
        power = 1
        while n % 10**power != n:
            if not primetest(n % 10**power): return False
            power += 1
        while n > 0:
            if not primetest(n): return False
            n //= 10
        return True

    count = 0
    result = 0
    number = 11
    while count < 11:
        if is_truncatable_prime(number):
            count += 1
            result += number
        number += 2
    print(result)
    return result
