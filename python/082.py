from benchmark import benchmark

m = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]
@benchmark()
def min_path(mtrx):
    rows, cols = len(mtrx), len(mtrx[0])
    for col in reversed(range(cols-1)):
        col_sums = []
        for r in range(rows):
            val = mtrx[r][col]
            if col_sums: col_sums.append(val + col_sums[-1])

        for row in range(rows):
            if row == 0:
                out = []
                for r in range(rows):
                    out.append(col_sums[r] + mtrx[r][col+1])
                mtrx[row][col] = min(out)
                continue
            out = []
            for r in range(rows):
                if r == 0:
                    out.append(col_sums[row] + mtrx[r][col+1])
                elif r < row:
                    out.append(col_sums[row] - col_sums[r-1]+ mtrx[r][col+1])
                else:
                    out.append(col_sums[r] - col_sums[row-1]+ mtrx[r][col+1])
            mtrx[row][col] = min(out)
    return min(mtrx[r][0] for r in range(rows))


def main():
    matrix = []
    with open('081.txt', 'r') as mtrx:
        for line in mtrx:
            matrix.append( list(map(int, line[:-1].split(','))) )
        x = min_path(matrix)
        print(x)


if __name__ == '__main__':
    main()     

