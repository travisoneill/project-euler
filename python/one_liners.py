from functools import reduce
from math import sqrt, log, factorial

inputs = {
    1: 1000,
    5: 20,
    6: 100,
    8: (13, "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"),
    9: 1000,
    10: 2000000,
    15: (20, 20)
    45: 30000,
    48: 1000
}

problem1 = lambda n: sum([x for x in range(n) if not x % 5 or not x % 3])

problem5 = lambda n: reduce(lambda a, b: a * b, [i ** int(log(n, i)) for i in (x for x in range(2, n) if not [y for y in range(2, int(sqrt(x))+1) if x % y == 0])])

problem6 = lambda n: sum([x for x in range(n+1)]) ** 2 - sum([x**2 for x in range(n+1)])

problem8 = lambda t: max([reduce(lambda x, y: x * y, map(int, list(t[1][i-t[0]:i]))) for i in range(t[0], len(t[1])+1)])

problem9 = lambda n: [(a, int(sqrt(c**2 - a**2)), c) for a in range(1, int(0.3*n+1)) for c in range(int(0.4*n), int(0.5*n+1)) if abs(sqrt(c**2 - a**2) - int(sqrt(c**2 - a**2))) % 1 < 0.0001 and abs(a + sqrt(c**2 - a**2) + c - n) < 0.0001]

problem10 = lambda n: sum([x for x in range(2, n) if not [y for y in range(2, int(sqrt(x))+1) if x % y == 0]])

problem15 = lambda rows, columns: factorial(rows + columns) // ( factorial(rows) * factorial(columns) )

problem38 = lambda: [ n*100002 for n in reversed(range(9182, 10000)) if max(Counter(str(n*100002)).values()) == 1 and not Counter(str(n*100002))['0'] ][0]

problem45 = lambda arbitrary: [n*(2*n -1) for n in range(144, arbitrary) if sqrt(48*n**2 - 24*n + 1) % 6 == 5][0]

problem48 = lambda n: sum([i**i % 10**10 for i in range(1, n+1)]) % 10**10

def get_lambda(problem):
    def wrapper(num):
        arg = inputs[num]
        func = globals()['problem{}'.format(num)]
        return func(arg)
    return wrapper

@get_lambda
def euler(num):
    pass

@
