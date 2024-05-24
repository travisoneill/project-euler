import math
from simplemath import is_perfect_square, int_sqrt
from benchmark import benchmark
from primesandfactors import prime_factors, primes2


def test(n, v=False):
    i = 1
    count = 0
    # hyp
    while i < n // 2:
        diff = 2*(n//2)**2 - i*i
        sqrt = math.sqrt(diff)
        # if  is_perfect_square(diff):
        if not sqrt % 1:
            count += 1
            if v:
                # print(i/n, int(sqrt)/n)
                print(i, int(sqrt))
        i += 1
    return count


def test3(n, v=False):
    hyp_sq = 2*n**2
    i = 1
    count = 0
    while i < n:
        root = math.sqrt(hyp_sq - i*i)
        # test = math.isqrt(hyp_sq - i*i - 1)
        if root%1 == 0:
            count += 1
            if v:
                print(i, math.isqrt(hyp_sq - i*i))
        i+= 1
    return count


def test4(n, squares):
    hyp_sq = 2*n**2
    i = 1
    count = 0
    while i < n:
        if hyp_sq - i*i in squares:
            count += 1
        i+= 1
    return count


def test2(a,b,c,d):
    x = 2*5**a*13**b*17**c*29**d
    return test(x)


@benchmark()
def run(n, target, v=False):
    squares = set()
    count = 0
    lim = int(math.sqrt(2*n**2))
    for i in range(lim+1):
        squares.add(i*i)

    out = set()
    for i in range(0, n):
        if i % (n//100) == 0:
            print(i)
        t = test4(i, squares)
        if t == 13:
            count += 1
            if v:
                print(i, t, prime_factors(i))
            out.add(i)
    print(count)
    return out


def get_count(base, limit, primes):
    temp_count = 0
    s = 0
    for mult in range(1, (limit // base)+1):
        valid = True
        for mod in primes:
            if mod > mult:
                break
            if mult % mod == 0:
                valid = False
                break
        if valid:
            # print(base*mult, prime_factors(base*mult))
            # out.add(base*mult)
            temp_count += 1
            s += base*mult
    return temp_count, s

# (1,1,1)
# (4,2)
# 5*13
@benchmark()
def count_matches_13(limit, target):
    primes = [p for p in primes2(int(limit // 65)) if p%4 == 1]
    count = 0
    for i, p1 in enumerate(primes):
        if p1*primes[i+1]*primes[i+2] > limit:
            break
        for j in range(i+1, len(primes)):
            p2 = primes[j]
            for k in range(j+1, len(primes)):
                p3 = primes[k]
                base = p1*p2*p3
                if base > limit:
                    break
                c, _ = get_count(base, limit, primes)
                count += c
    
    for i, p1 in enumerate(primes):
        for j in range(i+1, len(primes)):
            p2 = primes[j]
            base = p1**4*p2
            if base > limit:
                break
            c, _ = get_count(base, limit, primes)
            count += c
    print(count)

# (3,2,1)
# (7,3)
# (10,2)
@benchmark()
def count_matches_52(limit):
    primes = [p for p in primes2(int(limit // 21125)) if p%4 == 1]
    p2max = math.isqrt(limit // (primes[0]**3*primes[1]))
    p1max = int(math.pow(limit // (primes[0]**2*primes[1]), 1/3))
    
    max_mult = limit // (primes[0]**3 * primes[1]**2 * primes[2])
    cache = [(0,0) for _ in range(max_mult+1)]
    rsum = 0
    count = 0
    for mult in range(1, max_mult+1):
        valid = True
        for mod in primes:
            if mod > mult:
                break
            if mult % mod == 0:
                valid = False
                break
        count += int(valid)
        rsum += int(valid) * mult
        cache[mult] = (count, rsum)
    
    count = 0
    total_sum = 0
    for p1 in primes:
        if p1 > p1max:
            break
        for p2 in primes:
            if p2 > p2max:
                break
            if p1 == p2:
                continue
            for p3 in primes:
                if p3 == p1 or p3 == p2:
                    continue
                base = p1**3 * p2**2 * p3
                if base > limit:
                    break
                m = limit // base
                c, s = cache[m]
                count += c
                total_sum += s * base
    
    for p1 in primes:
        if p1**7 > limit:
            break
        for p2 in primes:
            if p1 == p2:
                continue
            base = p1**7 * p2**3
            if base > limit:
                break
            m = limit // base
            c, s = cache[m]
            count += c
            total_sum += s * base
    
    for p1 in primes:
        if p1**10 > limit:
            break
        for p2 in primes:
            if p1 == p2:
                continue
            base = p1**10 * p2**2
            if base > limit:
                break
            m = limit // base
            c, s = cache[m]
            count += c
            total_sum += s * base
    print(count, total_sum)
