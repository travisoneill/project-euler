from collections import Counter

def get_grids():
    with open('096.txt', 'r') as grid_file:
        return [ list(map( int, list(''.join([grid_file.readline()[:-1] for _ in range(9)])))) for line in grid_file if not line[0].isdigit()]

def get_grid(n):
    with open('096.txt', 'r') as grid_file:
        for line in grid_file:
            if line[:-1] == 'Grid {}'.format(str(n) if n > 9 else '0' + str(n)):
                return list(map( int, list(''.join([grid_file.readline()[:-1] for _ in range(9)])) ))

def check(grid):
    if 0 in grid: return False
    if Counter(grid) != Counter([x for x in range(1,10) for y in range(1, 10)]): return False

# def row(n, grid):
#     pass

class Grid:
    __slots__ = ['data', 'cols', 'rows']
    def __init__(self, rows, cols, default_value=None, data=None):
        self.data = data or [ [ default_value for _ in range(cols) ] for _ in range(rows) ]
        self.cols = cols
        self.rows = rows

    def get_row(self, n):
        first = self.cols * n
        last = first + self.cols
        return self.data[first:last]

    def get_col(self, n):
        return self.data[n::self.cols]

    def all_rows(self):
        for i in range(self.rows):
            yield self.get_row(i)

    def all_cols(self):
        for i in range(self.cols):
            yield self.get_col(i)

    def get_slice(self, start, y, x):
        result = []
        for _ in range(y):
            for i in range(x):
                result.append(self.data[start + i])
            start += self.cols
        return result

    def get_val(self, x, y=None):
        if y == None: x, y = x
        return self.data[x * self.cols + y]

    def set_val(self, value, x, y=None):
        if y == None: x, y = x
        self.data[x * self.cols + y] = value

    def __str__(self):
        string = []
        division = 9
        spacing = 2
        space = ' ' * spacing
        line = '-' * ( ( spacing + 1 ) * ( self.cols + self.cols // division + 1 ) - spacing )
        for row in range(self.rows):
            if row % division == 0: string.append(line)
            row_string = ''
            for idx, n in enumerate(self.get_row(row)):
                if idx % division == 0: row_string += '|' + space
                row_string += str(n)
                row_string += space
            string.append(row_string + '|' + space)
        string.append(line)
        return '\n'.join(string)

class Sudoku:
    def __init__(self, data=None):
        self.board = Grid(9, 9, 0, data=data)
        # print(self)

    def get_box(self, n):
        start = (n // 3) * 27 + (n % 3) * 3
        return self.board.get_slice(start, 3, 3)

    def get_col(self, n):
        return self.board.get_col(n)

    def get_row(self, n):
        return self.board.get_row(n)

    @staticmethod
    def valid(lst):
        s = set()
        for n in lst:
            if n == 0: continue
            if n in s: return False
            s.add(n)
        return True

    def step(self):
        state = False
        for i in range(81):
            c = (i // 9, i % 9)
            if self.board.get_val(c) != 0: continue
            p = list(self.possibilities(i))
            if not p: return 'ERROR'
            if len(p) == 1:
                state = True
                self.board.set_val(p[0], c)
        # print('valid: {}'.format(self.board_valid()))
        # print('solved: {}'.format(self.board_solved()))
        # if state: print(self)
        return state

    def revert(self, data):
        print(self)
        print('REVERT')
        self.board.data = data
        print(self)

    def guess(self):
        saved = self.board.data[:]
        for target_size in range(2, 9):
            for i in range(81):
                p = self.possibilities(i)
                if len(p) == target_size:
                    c = (i // 9, i % 9)
                    print('P:' + str(p))
                    for n in p:
                        print(str(p), n)
                        self.board.set_val(n, c)
                        x = self.solve()
                        print(x)
                        if x != 'SOLVED':
                            self.revert(saved)
                        else:
                            return
                    return



    def board_valid(self):
        for col in self.board.all_cols():
            if not Sudoku.valid(col): return False
        for row in self.board.all_rows():
            if not Sudoku.valid(row): return False
        for i in range(9):
            if not Sudoku.valid(self.get_box(i)): return False
        return True

    def board_solved(self):
        for col in self.board.all_cols():
            if not Sudoku.done(col): return False
        for row in self.board.all_rows():
            if not Sudoku.done(row): return False
        for i in range(9):
            if not Sudoku.done(self.get_box(i)): return False
        return True

    @staticmethod
    def done(lst):
        return set(lst) == {1,2,3,4,5,6,7,8,9}

    @staticmethod
    def remaining(lst):
        return {1,2,3,4,5,6,7,8,9} - set(lst)

    def solve(self):
        # print(self)
        def loop():
            while True:
                x = self.step()
                if self.board_solved(): return 'SOLVED'
                if not x: return 'IMPASSE'
                if x == 'ERROR': return 'ERROR'
                if not self.board_valid(): return 'ERROR'
                if not self.step(): return 'PROGRESS'
                # print('SOLVED!  score: {}'.format(self.score()))

        return loop()


    def score(self):
        return sum(self.board.get_slice(0, 1, 3))

    def possibilities(self, n):
        c = (n // 9, n % 9)
        if self.board.get_val(c) != 0: return set()
        box = self.get_box(3 * (n // 27) + n % 9 // 3)
        row = self.get_row(n // 9)
        col = self.get_col(n % 9)
        return self.remaining(row) & self.remaining(col) & self.remaining(box)

    def __str__(self):
        return self.board.__str__()


grids = get_grids()
g = Sudoku(grids[2])
#
def run():
    for grid in grids:
        g = Sudoku(grid)
        print(g.solve())
