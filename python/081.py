matrix = []
with open('081.txt', 'r') as mtrx:
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

def min_val(x, y):
    if x and y: return min(x, y)
    if x and not y: return min(x, float('inf'))
    if y and not x: return min(y, float('inf'))
    return 0

def min_path(mtrx):
    for y in reversed(range(len(mtrx))):
        for x in reversed(range(len(mtrx[0]))):
            c = (y, x)
            v = get_val(mtrx,c)
            d = down(mtrx, c)
            r = right(mtrx, c)
            mtrx[y][x] = v + min_val(r, d)
    return mtrx[0][0]
