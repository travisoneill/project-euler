matrix = []
with open('081.txt', 'r') as mtrx:
    for line in mtrx:
        matrix.append( list(map(int, line[:-1].split(','))) )

mtrx2 = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331]
]
