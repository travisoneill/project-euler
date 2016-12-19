from graph import Graph, Vertex

def min_pos(lst):
    m = max(lst)
    for el in lst:
        if el < m and el > 0:
            m = el
    return m

def minimize(mtrx):
    min_weight = 0
    for i in range(len(mtrx[0])):
        m = mtrx[i][0:i+1]
        print(m)
        min_weight += min_pos(m)
        print(min_pos(m))
    print(min_weight)

adj_mtrx = []
with open('107.txt', 'r') as mtrx:
    for line in mtrx:
        adj_mtrx.append(list(map(lambda s: int(s) if s.isdigit() else 0, line.split(','))))



test_case = [
    [00, 16, 12, 21, 00, 00, 00],
    [16, 00, 00, 17, 20, 00, 00],
    [12, 00, 00, 28, 00, 31, 00],
    [21, 17, 28, 00, 18, 19, 23],
    [00, 20, 00, 18, 00, 00, 11],
    [00, 00, 31, 19, 00, 00, 27],
    [00, 00, 00, 23, 11, 27, 00]
]

test_case2 = [
    [00, 16, 12, 00, 00, 00, 00],
    [16, 00, 00, 17, 00, 00, 00],
    [12, 00, 00, 00, 00, 00, 00],
    [21, 17, 28, 00, 18, 19, 00],
    [00, 20, 00, 18, 00, 00, 11],
    [00, 00, 31, 19, 00, 00, 00],
    [00, 00, 00, 23, 11, 27, 00]
]

test_case3 = [
    [00, 16, 12, 00, 00, 00, 00],
    [16, 00, 00, 17, 00, 00, 00],
    [12, 00, 00, 00, 00, 00, 00],
    [00, 17, 00, 00, 18, 19, 00],
    [00, 00, 00, 18, 00, 00, 11],
    [00, 00, 00, 19, 00, 00, 00],
    [00, 00, 00, 00, 11, 00, 00]
]
