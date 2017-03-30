from functools import reduce

score = lambda letter: 0 if letter == '"' else ord(letter) - 64
def run():
    with open('022.txt', 'r') as f:
        total = 0
        for line in f:
            words = line.split(',')
            for idx, word in enumerate(sorted(words)):
                total += reduce(lambda x, y: x + score(y), word, 0) * (idx+1)
        print(total)

words = []
with open('022.txt', 'r') as f:
    for line in f:
        words += line.split(',')
