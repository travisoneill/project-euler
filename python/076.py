from benchmark import benchmark

# def nx(n, m):
#     if m == 2:
#         return n // 2 + 1
#     else:
#         return sum([nx(n - i, m - 1) for i in reversed(range(0, n+1, m))])
#
#
# def nx2(n, m):
#     if m == 2:
#         return n // 2 + 1
#     else:
#         sm = 0
#         for i in reversed(range(0, n+1, m)):
#             sm += nx2(n - i, m - 1)
#         return sm

from collections import defaultdict
cache = defaultdict(dict)
def nx3(n, m):
    cached = cache[n].get(m)
    if cached:
        return cached
    if m == 2:
        return n // 2 + 1
    else:
        sm = 0
        for i in reversed(range(0, n+1, m)):
            res = nx3(n - i, m - 1)
            cache[n-i][m-1] = res
            sm += res
        return sm


@benchmark()
def number_of_sumnations(n):
    return nx3(n, n-1)


if __name__ == '__main__':
    number_of_sumnations(100)

# def num_ways_to_make(value, coin_set=None, prnt=False):
#     if value < 2: return 0
#
#     coin_set = coin_set or [ n for n in reversed(range(1, value)) ]
#     # Make initial coin list
#     coins = []
#     remaining_value = value
#     for idx in range(len(coin_set)):
#         coins.append(remaining_value // coin_set[idx])
#         remaining_value -= coin_set[idx] * coins[idx]
#     # Iterate through all possibilities and count
#     count = 1
#     while True:
#         if prnt:
#             print_coins(coins, coin_set)
#         if sum(coins[:-1]) == 0:
#             break
#         count += 1
#         coins = step(coins, coin_set)
#     return count
#
# def print_coins(coins, coin_set):
#     string = ''
#     # print(coins)
#     for idx, n in enumerate(coins):
#         val = len(coins) - idx
#         string += (str(coin_set[idx]) + ' ') * n
#     print(string)
#
# def step(coins, coin_set):
#     for idx in reversed(range(len(coins) - 1)):
#         if coins[idx] != 0:
#             break
#
#     coins[idx] -= 1
#     remaining_value = coin_set[idx] + coins[-1]
#     coins[-1] = 0
#     idx += 1
#     while remaining_value > 0:
#         coin = coin_set[idx]
#         num_coins = remaining_value // coin
#         coins[idx] += num_coins
#         remaining_value -= num_coins * coin
#         idx += 1
#     return coins

# from math import factorial
# def simplex(n, d):
#     out = 1
#     for i in range(d):
#         out *= n + i
#     return out / factorial(d)
