from collections import Counter
from functools import reduce

def value(card):
    values = { 'T': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12 }
    suits = { 'C': 0, 'D': 1, 'H': 2, 'S': 3 }
    v = values.get(card[0]) or int(card[0]) - 2
    s = suits.get(card[1])
    return s * 13 + v

def hand_eval(hand):
    rank = { 'RF': 9, 'SF': 8, '4K': 7, 'FH': 6, 'FL': 5, 'ST': 4, '3K': 3, '2P': 2, '2K': 1, 'HC': 0 }
    score = []
    suits = list({ x // 13 for x in hand })
    values = sorted([x % 13 + 2 for x in hand])
    counts = {values.count(card) for card in values}
    flush = len(suits) == 1
    straight = len(counts) == 1 and ( values[-1] - values[0] == 4 or values == [2,3,4,5,14] )
    if straight and flush:
        val = 9 if values[0] == 8 else 8
        score.append(val)
        score.append(values[-1])
        score.append(suits[0])
    elif flush:
        score.append(5)
        score.append(values[-1])
        score.append(suits[0])
    elif straight:
        score.append(4)
        score.append(values[1] + 3)

    values = sorted(values, key=lambda x: values.count(x))
    p_score = reduce(lambda x,y: x + y, [values.count(x) for x in values])

    if p_score == 17:
        score.append(7)
        score.append(values[-1])
    elif p_score == 13:
        score.append(6)
        score.append(values[-1])
        score.append(values[0])
    elif p_score == 11:
        score.append(3)
        score.append(values[-1])
        score.append(values[1])
        score.append(values[0])
    elif p_score == 9:
        score.append(2)
        score.append(values[-1])
        score.append(values[-3])
        score.append(values[0])
    elif p_score == 7:
        score.append(1)
        score.append(values[-1])
        score.append(values[2])
        score.append(values[1])
        score.append(values[0])
    elif p_score == 5:
        score.append(0)
        score.append(values[4])
        score.append(values[3])
        score.append(values[2])
        score.append(values[1])
        score.append(values[0])
    return score

def compare(hand1, hand2):
    score1 = hand_eval(hand1)
    score2 = hand_eval(hand2)
    for i in range(6):
        if score1[i] > score2[i]:
            return 1
        elif score1[i] < score2[i]:
            return 0

with open('54.txt', 'r') as f:
    count = 0
    for line in f:
        cards = line.split()
        hand1 = list(map(value, cards[:5]))
        hand2 = list(map(value, cards[5:]))
        count += compare(hand1, hand2)
    print(count)
