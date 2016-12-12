from math import sqrt
from functools import reduce
triangular = lambda n: (n**2 + n) // 2
inverse_triangular = lambda n: (sqrt(8*n+1)-1) / 2
tri_word = lambda word: inverse_triangular(reduce(lambda x,y: x + ord(y) - 64, word, 0)) % 1 == 0

def run():
    with open('042.txt', 'r') as f:
        count = 0
        for line in f:
            count += sum( map( tri_word, line.split('","')[:-1] )  )
        print(count)

# ONE LINER ATTEMPT
# tri_word = lambda word: (sqrt(8 * reduce(lambda x,y: x + ord(y) - 64, word, 0) + 1) - 1) / 2 % 1 == 0
# with open('042.txt', 'r') as f:
#     count = 0
#     for line in f:
#         # count += sum( map( tri_word, line.split('","')[:-1] )  )
#         count += sum( map( lambda word: (sqrt(8 * reduce(lambda x,y: x + ord(y) - 64, word, 0) + 1) - 1) / 2 % 1 == 0, line.split('","')[:-1] )  )
#     print(count)
