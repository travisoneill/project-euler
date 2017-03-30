from collections import Counter
# Product Must be > 918273645 from example given in problem
# Must be >9 from example, and number must have 9 as first digit
# Must be 4 digit or sum wont add to 9 digits

#ONE LINER
problem38 = lambda: [ n*100002 for n in reversed(range(9182, 10000)) if max(Counter(str(n*100002)).values()) == 1 and not Counter(str(n*100002))['0'] ][0]

def is_pandigital(n):
    if n // 10**8 < 1 or n // 10**8 > 9: return False
    idx = [False] * 10
    while n > 0:
        dig = n % 10
        if dig == 0 or idx[dig]: return False
        idx[dig] = True
        n //= 10
    return True

for n in reversed(range(9182, 10000)):
    if is_pandigital(n*100002):
        print(n*100002)
        break
