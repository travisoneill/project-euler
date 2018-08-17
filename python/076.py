from benchmark import benchmark

def nx(n, m):
    if m == 2:
        return n // 2 + 1
    else:
        return sum([nx(n - i, m - 1) for i in reversed(range(0, n+1, m))])


@benchmark()
def number_of_sumnations(n):
    return nx(n, n-1)

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
#
# def n2(n):
#     return n // 2 + 1
#
# def n3(n):
#     return sum([n2(n - i) for i in reversed(range(0, n+1, 3))])
#
# def nn3(n):
#     div = n // 3
#     mod = n % 3
#     count = div + 1
#     sm = 3 * ((div**2 + div) // 2) + (mod * count)
#     odd_count = count // 2 + (count % 2 == 1 and n % 2 == 1)
#     gain = odd_count // 2
#     quot = sm // 2 - gain
#     return quot + count
#
# def n4(n):
#     return sum([n3(n - i) for i in reversed(range(0, n+1, 4))])
#
# def n5(n):
#     return sum([n4(n - i) for i in reversed(range(0, n+1, 5))])
#
# def n6(n):
#     return sum([n5(n - i) for i in reversed(range(0, n+1, 6))])
#
# def n7(n):
#     return sum([n6(n - i) for i in reversed(range(0, n+1, 7))])
#
# def n8(n):
#     return sum([n7(n - i) for i in reversed(range(0, n+1, 8))])
#
# def n9(n):
#     return sum([n8(n - i) for i in reversed(range(0, n+1, 9))])
#
# def n10(n):
#     return sum([n9(n - i) for i in reversed(range(0, n+1, 10))])
