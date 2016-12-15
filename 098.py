from collections import defaultdict, Counter
from math import log10, sqrt

d = defaultdict(lambda: [], {})
with open('098.txt', 'r') as file1:
    for line in file1:
        for word in line[:-1].split(','):
            word = word[1:-1]
            d[''.join(sorted(word))].append(word)


def map_ints(num, string):
    obj = {}
    num = str(num)
    for i in range(len(string)):
        obj[string[i]] = num[i]
        obj[num[i]] = string[i]
    if len(set(obj.keys())) != len(obj.keys()) or len(set(obj.values())) != len(obj.values()):
        return False
    return obj

def transform(obj, word):
    res = ''
    for ltr in word:
        res += obj[ltr]
    if int(res) in squares[len(word)]:
        return int(res)
    else:
        return None
        
def find_square_anagrams():
    anagrams = { k: v for k, v in d.items() if len(v) > 1 }
    max_length = max([ max(map(len, x)) for x in anagrams.values() ])
    anagrams = sorted(anagrams.values(), key=lambda x: len(x[0]), reverse=True)
    squares = defaultdict(lambda: [], {})
    for i in range(1, 31623):
        squares[int(log10(i*i)) + 1].append(i*i)

    for pair in anagrams:
        word1, word2 = pair[0], pair[1]
        mapp = [ map_ints(n, word1) for n in squares[len(word1)] if map_ints(n, word1) ]
        res = [ transform(obj, word2) for obj in mapp if transform(obj, word2) ]
        if res: print(word1, word2, res)
