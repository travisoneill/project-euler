from benchmark import benchmark
from simplemath import int_log10

@benchmark()
def run(limit):
    step = 1
    num = 1
    denom = 2
    count = 0
    for _ in range(limit):
        if int_log10(denom + num) > int_log10(denom):
            count += 1
        num, denom = denom, ( denom * denom + step ) // num
        step *= -1
    print(count)
