a = [
[131, 673, 234, 103, 18 ],
[201, 96,  342, 965, 150],
[630, 803, 746, 422, 111],
[537, 699, 497, 121, 956],
[805, 732, 524, 37,  331]
]

class Matrix:
    # __slots__ = []
    def __init__(self)

matrix = []
with open('082.txt', 'r') as mtrx:
    for line in mtrx:
        matrix.append( list(map(int, line[:-1].split(','))) )

def down(mtrx, coord):
    h = len(mtrx)
    if coord[0] + 1 < h:
        return get_val( mtrx, (coord[0]+1, coord[1]))

def right(mtrx, coord):
    w = len(mtrx[0])
    if coord[1] + 1 < w:
        return get_val(mtrx, (coord[0], coord[1]+1))

def get_val(mtrx, coord):
    y, x = coord
    row =  mtrx[y:y+1][0:1]
    if row:
        col = row[0][x:x+1]
        if col:
            return col[0]

def current_column(mtrx, coord):
    pass
