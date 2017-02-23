from benchmark import benchmark
from simplemath import digital_sum

def cont_frac_e(length):
    e = [2]
    n = 2
    for i in range(1, length):
        if i % 3 == 2:
            e.append(n)
            n += 2
        else:
            e.append(1)
    return e

def fraction(cont_frac):
    d, n = 1, cont_frac[-1]
    for x in reversed(cont_frac[:-1]):
        prev_n = n
        prev_d = d
        d = prev_n
        n = x * d + prev_d
    return (n, d)

@benchmark()
def run(n):
    e = cont_frac_e(n)
    num = fraction(e)[0]
    return digital_sum(num)
