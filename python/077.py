from primesandfactors import primes2

def num_ways_to_make(value, coin_set=None, prnt=False):
    if value < 2: return 0

    coin_set = coin_set or [ n for n in reversed(range(1, value)) ]
    # Make initial coin list
    coins = []
    remaining_value = value
    for idx in range(len(coin_set)):
        coins.append(remaining_value // coin_set[idx])
        remaining_value -= coin_set[idx] * coins[idx]
    # Iterate through all possibilities and count
    count = 1
    while True:
        if prnt and coins[-1] == 0:
            print_coins(coins, coin_set)
        if sum(coins[:-1]) == 0:
            break
        if coins[-1] == 0:
            count += 1
        coins = step(coins, coin_set)
    return count

def print_coins(coins, coin_set):
    string = ''
    # print(coins)
    for idx, n in enumerate(coins):
        val = len(coins) - idx
        string += (str(coin_set[idx]) + ' ') * n
    print(string)

def step(coins, coin_set):
    for idx in reversed(range(len(coins) - 1)):
        if coins[idx] != 0:
            break

    coins[idx] -= 1
    remaining_value = coin_set[idx] + coins[-1]
    coins[-1] = 0
    idx += 1
    while remaining_value > 0 and idx < len(coin_set):
        coin = coin_set[idx]
        num_coins = remaining_value // coin
        coins[idx] += num_coins
        remaining_value -= num_coins * coin
        idx += 1
    # print(coins)
    return coins


def prime_sumnations(num):
    return num_ways_to_make(num, list(reversed([p for p in primes2(num)])) + [1])


if __name__ == '__main__':
    i = 10
    while True:
        if prime_sumnations(i) >= 5000:
            print(i)
            break
        i += 1
