
from benchmark import benchmark
from itertools import combinations_with_replacement


@benchmark()
def run(lim):
    sq = {1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600}
    sqdig = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
    fact = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]
    tot = 0
    for c in combinations_with_replacement(sqdig, lim):
        if sum(c) in sq:
            arr, perms = get_perms(c, fact[lim])
            tot += perm_sum(arr, perms)
    return tot


sqdig = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
inv_sq = [0] * 82
for i, s in enumerate(sqdig):
    inv_sq[s] = i


def get_perms(arr, fact):
    out = [0] * len(arr)
    counts = [0] * 10
    perms = fact
    for i, sq in enumerate(arr):
        inv = inv_sq[sq]
        out[i] = inv
        counts[inv] += 1
        perms //= counts[inv]
    return out, perms


def perm_sum(arr, perms):
    reps = perms / len(arr)
    x = int(reps * sum(arr))
    out = 0
    for _ in range(len(arr)):
        out *= 10
        out += x
    return out
