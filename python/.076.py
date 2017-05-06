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
        if prnt: print_coins(coins)
        if sum(coins[:-1]) == 0: break
        count += 1
        coins = step(coins, coin_set)
    return count

def print_coins(coins):
    string = ''
    for idx, n in enumerate(coins):
        val = len(coins) - idx
        string += (str(val) + ' ') * n
    print(string)

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

n = num_ways_to_make

'''
19 1

18 2
18 1 1

17 3
17 2 1
17 1 1 1

16 4
16 3 1
16 2 2
16 2 1 1
16 1 1 1 1

15 5
15 4 1
15 3 2
15 3 1 1
15 2 2 1
15 2 1 1 1
15 1 1 1 1 1

14 6
14 5 1
14 4 2
14 4 1 1
14 3 3
14 3 2 1
14 3 1 1 1
14 2 2 2
14 2 2 1 1
14 2 1 1 1 1
14 1 1 1 1 1 1

13 7
13 6 1
13 5 2
13 5 1 1
13 4 3
13 4 2 1
13 4 1 1 1
13 3 3 1
13 3 2 2
13 3 2 1 1
13 3 1 1 1 1
13 2 2 2 1
13 2 2 1 1 1
13 2 1 1 1 1 1
13 1 1 1 1 1 1 1

12 8
12 7 1
12 6 2
12 6 1 1
12 5 3
12 5 2 1
12 5 1 1 1
12 4 4
12 4 3 1
12 4 2 2
12 4 2 1 1
12 4 1 1 1 1
12 3 3 2
12 3 3 1 1
12 3 2 2 1
12 3 2 1 1 1
12 3 1 1 1 1 1
12 2 2 2 2
12 2 2 2 1 1
12 2 2 1 1 1 1
12 2 1 1 1 1 1 1
12 1 1 1 1 1 1 1 1

11 9
11 8 1
11 7 2
11 7 1 1
11 6 3
11 6 2 1
11 6 1 1 1
11 5 4
11 5 3 1
11 5 2 2
11 5 2 1 1
11 5 1 1 1 1
11 4 4 1
11 4 3 2
11 4 3 1 1
11 4 2 2 1
11 4 2 1 1 1
11 4 1 1 1 1 1
11 3 3 3
11 3 3 2 1
11 3 3 1 1 1
11 3 2 2 2
11 3 2 2 1 1
11 3 2 1 1 1 1
11 3 1 1 1 1 1 1
11 2 2 2 2 1
11 2 2 2 1 1 1
11 2 2 1 1 1 1 1
11 2 1 1 1 1 1 1 1
11 1 1 1 1 1 1 1 1 1

10 10
10 9 1
10 8 2
10 8 1 1
10 7 3
10 7 2 1
10 7 1 1 1
10 6 4
10 6 3 1
10 6 2 2
10 6 2 1 1
10 6 1 1 1 1
10 5 5
10 5 4 1
10 5 3 2
10 5 3 1 1
10 5 2 2 1
10 5 2 1 1 1
10 5 1 1 1 1 1
10 4 4 2
10 4 4 1 1
10 4 3 3
10 4 3 2 1
10 4 3 1 1 1
10 4 2 2 2
10 4 2 2 1 1
10 4 2 1 1 1 1
10 4 1 1 1 1 1 1
10 3 3 3 1
10 3 3 2 2
10 3 3 2 1 1
10 3 3 1 1 1 1
10 3 2 2 2 1
10 3 2 2 1 1 1
10 3 2 1 1 1 1 1
10 3 1 1 1 1 1 1 1
10 2 2 2 2 2
10 2 2 2 2 1 1
10 2 2 2 1 1 1 1
10 2 2 1 1 1 1 1 1
10 2 1 1 1 1 1 1 1 1
10 1 1 1 1 1 1 1 1 1 1

9 9 2
9 9 1 1
9 8 3
9 8 2 1
9 8 1 1 1
9 7 4
9 7 3 1
9 7 2 2
9 7 2 1 1
9 7 1 1 1 1
9 6 5
9 6 4 1
9 6 3 2
9 6 3 1 1
9 6 2 2 1
9 6 2 1 1 1
9 6 1 1 1 1 1
9 5 5 1
9 5 4 2
9 5 4 1 1
9 5 3 3
9 5 3 2 1
9 5 3 1 1 1
9 5 2 2 2
9 5 2 2 1 1
9 5 2 1 1 1 1
9 5 1 1 1 1 1 1
9 4 4 3
9 4 4 2 1
9 4 4 1 1 1
9 4 3 3 1
9 4 3 2 2
9 4 3 2 1 1
9 4 3 1 1 1 1
9 4 2 2 2 1
9 4 2 2 1 1 1
9 4 2 1 1 1 1 1
9 4 1 1 1 1 1 1 1
9 3 3 3 2
9 3 3 3 1 1
9 3 3 2 2 1
9 3 3 2 1 1 1
9 3 3 1 1 1 1 1
9 3 2 2 2 2
9 3 2 2 2 1 1
9 3 2 2 1 1 1 1
9 3 2 1 1 1 1 1 1
9 3 1 1 1 1 1 1 1 1
9 2 2 2 2 2 1
9 2 2 2 2 1 1 1
9 2 2 2 1 1 1 1 1
9 2 2 1 1 1 1 1 1 1
9 2 1 1 1 1 1 1 1 1 1
9 1 1 1 1 1 1 1 1 1 1 1

8 8 4
8 8 3 1
8 8 2 2
8 8 2 1 1
8 8 1 1 1 1
8 7 5
8 7 4 1
8 7 3 2
8 7 3 1 1
8 7 2 2 1
8 7 2 1 1 1
8 7 1 1 1 1 1
8 6 6
8 6 5 1
8 6 4 2
8 6 4 1 1
8 6 3 3
8 6 3 2 1
8 6 3 1 1 1
8 6 2 2 2
8 6 2 2 1 1
8 6 2 1 1 1 1
8 6 1 1 1 1 1 1
8 5 5 2
8 5 5 1 1
8 5 4 3
8 5 4 2 1
8 5 4 1 1 1
8 5 3 3 1
8 5 3 2 2
8 5 3 2 1 1
8 5 3 1 1 1 1
8 5 2 2 2 1
8 5 2 2 1 1 1
8 5 2 1 1 1 1 1
8 5 1 1 1 1 1 1 1
8 4 4 4
8 4 4 3 1
8 4 4 2 2
8 4 4 2 1 1
8 4 4 1 1 1 1
8 4 3 3 2
8 4 3 3 1 1
8 4 3 2 2 1
8 4 3 2 1 1 1
8 4 3 1 1 1 1 1
8 4 2 2 2 2
8 4 2 2 2 1 1
8 4 2 2 1 1 1 1
8 4 2 1 1 1 1 1 1
8 4 1 1 1 1 1 1 1 1
8 3 3 3 3
8 3 3 3 2 1
8 3 3 3 1 1 1
8 3 3 2 2 2
8 3 3 2 2 1 1
8 3 3 2 1 1 1 1
8 3 3 1 1 1 1 1 1
8 3 2 2 2 2 1
8 3 2 2 2 1 1 1
8 3 2 2 1 1 1 1 1
8 3 2 1 1 1 1 1 1 1
8 3 1 1 1 1 1 1 1 1 1
8 2 2 2 2 2 2
8 2 2 2 2 2 1 1
8 2 2 2 2 1 1 1 1
8 2 2 2 1 1 1 1 1 1
8 2 2 1 1 1 1 1 1 1 1
8 2 1 1 1 1 1 1 1 1 1 1
8 1 1 1 1 1 1 1 1 1 1 1 1

7 7 6
7 7 5 1
7 7 4 2
7 7 4 1 1
7 7 3 3
7 7 3 2 1
7 7 3 1 1 1
7 7 2 2 2
7 7 2 2 1 1
7 7 2 1 1 1 1
7 7 1 1 1 1 1 1
7 6 6 1
7 6 5 2
7 6 5 1 1
7 6 4 3
7 6 4 2 1
7 6 4 1 1 1
7 6 3 3 1
7 6 3 2 2
7 6 3 2 1 1
7 6 3 1 1 1 1
7 6 2 2 2 1
7 6 2 2 1 1 1
7 6 2 1 1 1 1 1
7 6 1 1 1 1 1 1 1
7 5 5 3
7 5 5 2 1
7 5 5 1 1 1
7 5 4 4
7 5 4 3 1
7 5 4 2 2
7 5 4 2 1 1
7 5 4 1 1 1 1
7 5 3 3 2
7 5 3 3 1 1
7 5 3 2 2 1
7 5 3 2 1 1 1
7 5 3 1 1 1 1 1
7 5 2 2 2 2
7 5 2 2 2 1 1
7 5 2 2 1 1 1 1
7 5 2 1 1 1 1 1 1
7 5 1 1 1 1 1 1 1 1
7 4 4 4 1
7 4 4 3 2
7 4 4 3 1 1
7 4 4 2 2 1
7 4 4 2 1 1 1
7 4 4 1 1 1 1 1
7 4 3 3 3
7 4 3 3 2 1
7 4 3 3 1 1 1
7 4 3 2 2 2
7 4 3 2 2 1 1
7 4 3 2 1 1 1 1
7 4 3 1 1 1 1 1 1
7 4 2 2 2 2 1
7 4 2 2 2 1 1 1
7 4 2 2 1 1 1 1 1
7 4 2 1 1 1 1 1 1 1
7 4 1 1 1 1 1 1 1 1 1
7 3 3 3 3 1
7 3 3 3 2 2
7 3 3 3 2 1 1
7 3 3 3 1 1 1 1
7 3 3 2 2 2 1
7 3 3 2 2 1 1 1
7 3 3 2 1 1 1 1 1
7 3 3 1 1 1 1 1 1 1
7 3 2 2 2 2 2
7 3 2 2 2 2 1 1
7 3 2 2 2 1 1 1 1
7 3 2 2 1 1 1 1 1 1
7 3 2 1 1 1 1 1 1 1 1
7 3 1 1 1 1 1 1 1 1 1 1
7 2 2 2 2 2 2 1
7 2 2 2 2 2 1 1 1
7 2 2 2 2 1 1 1 1 1
7 2 2 2 1 1 1 1 1 1 1
7 2 2 1 1 1 1 1 1 1 1 1
7 2 1 1 1 1 1 1 1 1 1 1 1
7 1 1 1 1 1 1 1 1 1 1 1 1 1

6 6 6 2
6 6 6 1 1
6 6 5 3
6 6 5 2 1
6 6 5 1 1 1
6 6 4 4
6 6 4 3 1
6 6 4 2 2
6 6 4 2 1 1
6 6 4 1 1 1 1
6 6 3 3 2
6 6 3 3 1 1
6 6 3 2 2 1
6 6 3 2 1 1 1
6 6 3 1 1 1 1 1
6 6 2 2 2 2
6 6 2 2 2 1 1
6 6 2 2 1 1 1 1
6 6 2 1 1 1 1 1 1
6 6 1 1 1 1 1 1 1 1
6 5 5 4
6 5 5 3 1
6 5 5 2 2
6 5 5 2 1 1
6 5 5 1 1 1 1
6 5 4 4 1
6 5 4 3 2
6 5 4 3 1 1
6 5 4 2 2 1
6 5 4 2 1 1 1
6 5 4 1 1 1 1 1
6 5 3 3 3
6 5 3 3 2 1
6 5 3 3 1 1 1
6 5 3 2 2 2
6 5 3 2 2 1 1
6 5 3 2 1 1 1 1
6 5 3 1 1 1 1 1 1
6 5 2 2 2 2 1
6 5 2 2 2 1 1 1
6 5 2 2 1 1 1 1 1
6 5 2 1 1 1 1 1 1 1
6 5 1 1 1 1 1 1 1 1 1
6 4 4 4 2
6 4 4 4 1 1
6 4 4 3 3
6 4 4 3 2 1
6 4 4 3 1 1 1
6 4 4 2 2 2
6 4 4 2 2 1 1
6 4 4 2 1 1 1 1
6 4 4 1 1 1 1 1 1
6 4 3 3 3 1
6 4 3 3 2 2
6 4 3 3 2 1 1
6 4 3 3 1 1 1 1
6 4 3 2 2 2 1
6 4 3 2 2 1 1 1
6 4 3 2 1 1 1 1 1
6 4 3 1 1 1 1 1 1 1
6 4 2 2 2 2 2
6 4 2 2 2 2 1 1
6 4 2 2 2 1 1 1 1
6 4 2 2 1 1 1 1 1 1
6 4 2 1 1 1 1 1 1 1 1
6 4 1 1 1 1 1 1 1 1 1 1
6 3 3 3 3 2
6 3 3 3 3 1 1
6 3 3 3 2 2 1
6 3 3 3 2 1 1 1
6 3 3 3 1 1 1 1 1
6 3 3 2 2 2 2
6 3 3 2 2 2 1 1
6 3 3 2 2 1 1 1 1
6 3 3 2 1 1 1 1 1 1
6 3 3 1 1 1 1 1 1 1 1
6 3 2 2 2 2 2 1
6 3 2 2 2 2 1 1 1
6 3 2 2 2 1 1 1 1 1
6 3 2 2 1 1 1 1 1 1 1
6 3 2 1 1 1 1 1 1 1 1 1
6 3 1 1 1 1 1 1 1 1 1 1 1
6 2 2 2 2 2 2 2
6 2 2 2 2 2 2 1 1
6 2 2 2 2 2 1 1 1 1
6 2 2 2 2 1 1 1 1 1 1
6 2 2 2 1 1 1 1 1 1 1 1
6 2 2 1 1 1 1 1 1 1 1 1 1
6 2 1 1 1 1 1 1 1 1 1 1 1 1
6 1 1 1 1 1 1 1 1 1 1 1 1 1 1

5 5 5 5
5 5 5 4 1
5 5 5 3 2
5 5 5 3 1 1
5 5 5 2 2 1
5 5 5 2 1 1 1
5 5 5 1 1 1 1 1

5 5 4 4 2
5 5 4 4 1 1

5 5 4 3 3
5 5 4 3 2 1
5 5 4 3 1 1 1
5 5 4 2 2 2
5 5 4 2 2 1 1
5 5 4 2 1 1 1 1
5 5 4 1 1 1 1 1 1

5 5 3 3 3 1
5 5 3 3 2 2
5 5 3 3 2 1 1
5 5 3 3 1 1 1 1
5 5 3 2 2 2 1
5 5 3 2 2 1 1 1
5 5 3 2 1 1 1 1 1
5 5 3 1 1 1 1 1 1 1
5 5 2 2 2 2 2
5 5 2 2 2 2 1 1
5 5 2 2 2 1 1 1 1
5 5 2 2 1 1 1 1 1 1
5 5 2 1 1 1 1 1 1 1 1
5 5 1 1 1 1 1 1 1 1 1 1
5 4 4 4 3
5 4 4 4 2 1
5 4 4 4 1 1 1
5 4 4 3 3 1
5 4 4 3 2 2
5 4 4 3 2 1 1
5 4 4 3 1 1 1 1
5 4 4 2 2 2 1
5 4 4 2 2 1 1 1
5 4 4 2 1 1 1 1 1
5 4 4 1 1 1 1 1 1 1
5 4 3 3 3 2
5 4 3 3 3 1 1
5 4 3 3 2 2 1
5 4 3 3 2 1 1 1
5 4 3 3 1 1 1 1 1
5 4 3 2 2 2 2
5 4 3 2 2 2 1 1
5 4 3 2 2 1 1 1 1
5 4 3 2 1 1 1 1 1 1
5 4 3 1 1 1 1 1 1 1 1
5 4 2 2 2 2 2 1
5 4 2 2 2 2 1 1 1
5 4 2 2 2 1 1 1 1 1
5 4 2 2 1 1 1 1 1 1 1
5 4 2 1 1 1 1 1 1 1 1 1
5 4 1 1 1 1 1 1 1 1 1 1 1
5 3 3 3 3 3
5 3 3 3 3 2 1
5 3 3 3 3 1 1 1
5 3 3 3 2 2 2
5 3 3 3 2 2 1 1
5 3 3 3 2 1 1 1 1
5 3 3 3 1 1 1 1 1 1
5 3 3 2 2 2 2 1
5 3 3 2 2 2 1 1 1
5 3 3 2 2 1 1 1 1 1
5 3 3 2 1 1 1 1 1 1 1
5 3 3 1 1 1 1 1 1 1 1 1
5 3 2 2 2 2 2 2
5 3 2 2 2 2 2 1 1
5 3 2 2 2 2 1 1 1 1
5 3 2 2 2 1 1 1 1 1 1
5 3 2 2 1 1 1 1 1 1 1 1
5 3 2 1 1 1 1 1 1 1 1 1 1
5 3 1 1 1 1 1 1 1 1 1 1 1 1
5 2 2 2 2 2 2 2 1
5 2 2 2 2 2 2 1 1 1
5 2 2 2 2 2 1 1 1 1 1
5 2 2 2 2 1 1 1 1 1 1 1
5 2 2 2 1 1 1 1 1 1 1 1 1
5 2 2 1 1 1 1 1 1 1 1 1 1 1
5 2 1 1 1 1 1 1 1 1 1 1 1 1 1
5 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

4 4 4 4 4

4 4 4 4 3 1
4 4 4 4 2 2
4 4 4 4 2 1 1
4 4 4 4 1 1 1 1

                            7 1

                            6 2
                            6 1 1

                            5 3
                            5 2 1
                            5 1 1 1

                            4 4
4 4 4 3 3 2                 4 3 1  4 2 2
4 4 4 3 3 1 1               4 2 1 1
4 4 4 3 2 2 1               4 1 1 1 1
4 4 4 3 2 1 1 1
4 4 4 3 1 1 1 1 1
4 4 4 2 2 2 2
4 4 4 2 2 2 1 1
4 4 4 2 2 1 1 1 1
4 4 4 2 1 1 1 1 1 1
4 4 4 1 1 1 1 1 1 1 1

4 4 3 3 3 3
4 4 3 3 3 2 1
4 4 3 3 3 1 1 1
4 4 3 3 2 2 2
4 4 3 3 2 2 1 1
4 4 3 3 2 1 1 1 1
4 4 3 3 1 1 1 1 1 1
4 4 3 2 2 2 2 1
4 4 3 2 2 2 1 1 1
4 4 3 2 2 1 1 1 1 1
4 4 3 2 1 1 1 1 1 1 1
4 4 3 1 1 1 1 1 1 1 1 1
4 4 2 2 2 2 2 2
4 4 2 2 2 2 2 1 1
4 4 2 2 2 2 1 1 1 1
4 4 2 2 2 1 1 1 1 1 1
4 4 2 2 1 1 1 1 1 1 1 1
4 4 2 1 1 1 1 1 1 1 1 1 1
4 4 1 1 1 1 1 1 1 1 1 1 1 1

4 3 3 3 3 3 1
4 3 3 3 3 2 2
4 3 3 3 3 2 1 1
4 3 3 3 3 1 1 1 1
4 3 3 3 2 2 2 1
4 3 3 3 2 2 1 1 1
4 3 3 3 2 1 1 1 1 1
4 3 3 3 1 1 1 1 1 1 1
4 3 3 2 2 2 2 2
4 3 3 2 2 2 2 1 1
4 3 3 2 2 2 1 1 1 1
4 3 3 2 2 1 1 1 1 1 1
4 3 3 2 1 1 1 1 1 1 1 1
4 3 3 1 1 1 1 1 1 1 1 1 1
4 3 2 2 2 2 2 2 1
4 3 2 2 2 2 2 1 1 1
4 3 2 2 2 2 1 1 1 1 1
4 3 2 2 2 1 1 1 1 1 1 1
4 3 2 2 1 1 1 1 1 1 1 1 1
4 3 2 1 1 1 1 1 1 1 1 1 1 1
4 3 1 1 1 1 1 1 1 1 1 1 1 1 1
4 2 2 2 2 2 2 2 2
4 2 2 2 2 2 2 2 1 1
4 2 2 2 2 2 2 1 1 1 1
4 2 2 2 2 2 1 1 1 1 1 1
4 2 2 2 2 1 1 1 1 1 1 1 1
4 2 2 2 1 1 1 1 1 1 1 1 1 1
4 2 2 1 1 1 1 1 1 1 1 1 1 1 1
4 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
4 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1   1 4 10 19 30

3 3 3 3 3 3 2    (7 * 6)
3 3 3 3 3 3 1 1

3 3 3 3 3 2 2 1
3 3 3 3 3 2 1 1 1
3 3 3 3 3 1 1 1 1 1

3 3 3 3 2 2 2 2
3 3 3 3 2 2 2 1 1
3 3 3 3 2 2 1 1 1 1
3 3 3 3 2 1 1 1 1 1 1
3 3 3 3 1 1 1 1 1 1 1 1

3 3 3 2 2 2 2 2 1
3 3 3 2 2 2 2 1 1 1
3 3 3 2 2 2 1 1 1 1 1
3 3 3 2 2 1 1 1 1 1 1 1
3 3 3 2 1 1 1 1 1 1 1 1 1
3 3 3 1 1 1 1 1 1 1 1 1 1 1

3 3 2 2 2 2 2 2 2
3 3 2 2 2 2 2 2 1 1
3 3 2 2 2 2 2 1 1 1 1
3 3 2 2 2 2 1 1 1 1 1 1
3 3 2 2 2 1 1 1 1 1 1 1 1
3 3 2 2 1 1 1 1 1 1 1 1 1 1
3 3 2 1 1 1 1 1 1 1 1 1 1 1 1
3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

3 2 2 2 2 2 2 2 2 1
3 2 2 2 2 2 2 2 1 1 1
3 2 2 2 2 2 2 1 1 1 1 1
3 2 2 2 2 2 1 1 1 1 1 1 1
3 2 2 2 2 1 1 1 1 1 1 1 1 1
3 2 2 2 1 1 1 1 1 1 1 1 1 1 1
3 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1
3 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
3 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

2 2 2 2 2 2 2 2 2 2
2 2 2 2 2 2 2 2 2 1 1
2 2 2 2 2 2 2 2 1 1 1 1
2 2 2 2 2 2 2 1 1 1 1 1 1
2 2 2 2 2 2 1 1 1 1 1 1 1 1
2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
2 2 2 2 1 1 1 1 1 1 1 1 1 1 1 1
2 2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2 2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
'''