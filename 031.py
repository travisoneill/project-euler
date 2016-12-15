def num_ways_to_make(value, coin_set=[200, 100, 50, 20, 10, 5, 2, 1]):
    # Make initial coin list
    coins = []
    remaining_value = value
    for idx in range(len(coin_set)):
        coins.append(remaining_value // coin_set[idx])
        remaining_value -= coin_set[idx] * coins[idx]
    # Iterate through all possibilities and count
    count = 1
    while True:
        if sum(coins[:-1]) == 0: break
        count += 1
        coins = step(coins, coin_set)
    print(count)

def step(coins, coin_set):
    for idx in reversed(range( len(coins) - 1 )):
        if coins[idx] != 0: break
    coins[idx] -= 1
    remaining_value = coin_set[idx] + coins[-1]
    coins[-1] = 0
    idx += 1
    while remaining_value > 0:
        coin = coin_set[idx]
        num_coins = remaining_value // coin
        coins[idx] += num_coins
        remaining_value -= num_coins * coin
        idx += 1
    return coins
