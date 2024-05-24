import sys
from primesandfactors import prime_factors, miller_rabin
from benchmark import benchmark

def res(d):
    count = 0
    factors = sorted(set(prime_factors(d)))
    for i in range(2, d):
        if d % i == 0:
            continue
        resilient = True
        for f in factors:
            if i % f == 0:
                resilient = False
                break
        count += int(resilient)
        
    return count + 1, (count+1) /(d-1) 


@benchmark()
def count_primes(lim):
    count = 0
    for i in range(2, lim+1):
        if miller_rabin(i):
            count += 1
    return count

def possible(lim):
    i = 7
    while i <= lim:
        yield i
        i += (i-3) % 6



@benchmark()
def count_primes2(lim):
    count = 0
    for i in possible(lim):
        if miller_rabin(i):
            count += 1
    return count + 3

if __name__ == '__main__':
    x = count_primes2(int(sys.argv[1]))
    print(x)
