m = [
    [131, 673, 234, 103, 18],
    [201, 96, 342, 965, 150],
    [630, 803, 746, 422, 111],
    [537, 699, 497, 121, 956],
    [805, 732, 524, 37, 331],
]

def min_path(mtrx):
    rows, cols = len(mtrx), len(mtrx[0])
    col = len(mtrx[0]) - 2
    col_sums = []
    for r in range(rows):
        val = mtrx[r][col]
        if col_sums: col_sums.append(val + col_sums[-1])
        else: col_sums.append(val)
    print(col_sums)
    print('')

    for row in range(rows):
        if row == 0:
            out = []
            for r in range(rows):
                out.append(col_sums[r] + mtrx[r][col+1])
            print(out, min(out))
            continue
        out = []
        for r in range(rows):
            if r == 0:
                out.append(col_sums[row] + mtrx[r][col+1])
            elif r < row:
                out.append(col_sums[row] - col_sums[r-1]+ mtrx[r][col+1])
            else:
                out.append(col_sums[r] - col_sums[row-1]+ mtrx[r][col+1])
        print(out, min(out))

if __name__ == '__main__':
    min_path(m)         


    # [103, 1068, 1490, 1611, 1648]
    # [103, 965, 422, 121, 37]


# row 1
#     cs[1]
    
#     cs[1] - cs[0]
#     cs[2] - cs[0]
#     cs[3] - cs[0]
#     cs[4] - cs[0]

# row 2
#     cs[2]
#     cs[2] - cs[0]
    
#     cs[2] - cs[1]
#     cs[3] - cs[1]
#     cs[4] - cs[1]

# row 3
#     cs[3]
#     cs[3] - cs[0]
#     cs[3] - cs[1]
    
#     cs[3] - cs[2]
#     cs[4] - cs[2]

# row 4
#     cs[4]
#     cs[4] - cs[0]
#     cs[4] - cs[1]
#     cs[4] - cs[2]
    
#     cs[4] - cs[3]

    
