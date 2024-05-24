import math

from benchmark import benchmark
from collections import Counter

m = [
    [131, 673, 234, 103,  18],
    [201,  96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524,  37, 331],
]



def neighbors(N, r, c):
    poss = [(r, c+1), (r,c-1), (r+1, c), (r-1, c)]
    return [(r, c) for r, c in poss if r < N and c < N and r >= 0 and c >= 0]


def dfs(mtrx, row, col, target, min_val):
    N = len(mtrx)
    depth = mtrx[row][col]
    stack = [(row, col, depth, {(row, col)})]
    min_depth = depth + (mtrx[row+1][col] if col == N -1 else mtrx[row][col+1])
    temp_depth_to_node = {}
    exit_depth = min_depth - min_val
    while stack:
        r, c, depth, seen = stack.pop()
        if r + c == target:
            min_depth = min(min_depth, depth)
            continue
        elif depth >= exit_depth:
            continue
        elif (r, c) in temp_depth_to_node:
            temp_best = temp_depth_to_node[(r,c)]
            if depth > temp_best:
                continue
            temp_depth_to_node[(r,c)] = min(temp_best, depth)
        else:
            temp_depth_to_node[(r,c)] = depth
        for nr, nc in neighbors(N, r, c):
            if (nr, nc) not in seen:
                stack.append((nr, nc, depth + mtrx[nr][nc], seen.union({(nr, nc)})))
    return min_depth



def diag_row(mtrx, n):
    row, col = min(n, len(mtrx) - 1), max(n - len(mtrx) + 1, 0)
    while row >= 0 and col < len(mtrx):
        yield row, col
        row -= 1
        col += 1


@benchmark()
def min_path(mtrx):
    D = len(mtrx) * 2 - 2
    min_val = 0
    for i in reversed(range(D)):
        change = {}
        for r, c in diag_row(mtrx, i):
            d = dfs(mtrx, r, c, i+1, min_val)
            change[(r,c)] = d
        
        mm = math.inf
        for (r, c), val in change.items():
            mm = min(mm, val)
            mtrx[r][c] = val
        min_val = mm
    return mtrx[0][0]

def mprint(m):
    for r in m:
        print(r)
    print('')


def get_matrix():
    matrix = []
    with open('081.txt', 'r') as mtrx:
        for line in mtrx:
            matrix.append( list(map(int, line[:-1].split(','))) )
    return matrix

if __name__ == '__main__':
    m = get_matrix()
    x = min_path(m)
    print(x)
