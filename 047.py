from collections import defaultdict, deque
from math import sqrt

def f_count(n):
    count = defaultdict(int, {})
    i = 2
    while i < sqrt(n) + 1:
        if n % i == 0:
            count[i] += 1
            n //= i
        else:
            i += 1
    if n > 1: count[n] += 1
    return {k**v for k, v in count.items()}



q = deque([set(), set(), set(), set()])
i = 2
while True:
    q.append(f_count(i))
    if len(q) > 4: q.popleft()
    if len(q[0] | q[1] | q[2] | q[3]) == 16:
        print(i)
        break
    i += 1
