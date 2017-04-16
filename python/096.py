from collections import Counter
from benchmark import benchmark
import sys

class Sudoku(list):
    def __init__(self, lst=None):
        lst = lst or []
        super().__init__(lst)
        self.stack = []
        self.limit = Counter(self)[0]
        self.map = []
        # self.board = []

    def row(self, idx):
        return [ self[i] for i in range(9*idx, 9*idx+9) ]

    def col(self, idx):
        return [ self[i] for i in range(idx, len(self), 9) ]

    def box(self, idx):
        i = 27 * (idx // 3) + 3 * (idx % 3)
        return [self[i], self[i+1], self[i+2], self[i+9], self[i+10], self[i+11], self[i+18], self[i+19], self[i+20]]

    @staticmethod
    def check(lst):
        l = [n for n in lst if n]
        return len(l) == len(set(l))

    def merge(self):
        board = []
        idx = 0
        for sq in self:
            if sq != 0:
                board.append(sq)
            elif idx < len(self.stack):
                board.append(self.stack[idx])
                idx += 1
            else:
                board.append(0)
        return board

    def coord(self, idx):
        row = idx // 9
        col = idx % 9
        box = 3 * (row // 3) + col // 3
        return (row, col, box)

    def possibilities(self, idx):
        if self[idx]:
            return []
        else:
            r, c, b = self.coord(idx)
            arr = self.row(r) + self.col(c) + self.box(b)
            s = {x for x in range(1, 10)} - { x for x in arr if x > 0 }
        return sorted(s)

    def logic_step(self):
        for idx in range(81):
            p = self.possibilities(idx)
            if len(p) == 1:
                self[idx] = p[0]
                self.logic_step()
        self.limit = Counter(self)[0]

    def append(self, n):
        self.stack.append(n)

    def rotate_y(self):
        return Sudoku(self[27:] + self[:27])

    def rotate_x(self):
        res = []
        for i in range(9):
            r = self.row(i)
            for j in range(9):
                idx = (j + 3) % 9
                res.append(r[idx])
        return Sudoku(res)




    def pop(self):
        self.stack.pop()

    def next(self):
        if self.stack[-1] == 0:
            self.stack.pop()
        if self.stack[-1] < 9:
            self.stack[-1] += 1
        else:
            self.stack.pop()
            self.next()

    def next2(self):
        idx = len(self.stack) - 1
        num = self.stack[-1]
        pos = self.map[idx]
        lim = len(pos) - 1
        # import pdb; pdb.set_trace()
        i = pos.index(num)
        # import pdb; pdb.set_trace()
        if self.stack[-1] == 0:
            self.stack.pop()
        if self.stack[-1] < pos[-2]:
            i2 = i + 1
            self.stack[-1] = pos[i2]
        else:
            self.stack.pop()
            self.next2()

    def poss_map(self):
        mp = []
        for i in range(81):
            if self[i] == 0:
                mp.append(self.possibilities(i) + [0])
        mp.append([0])
        return mp

    def valid(self):
        board = Sudoku(self.merge())
        ch = Sudoku.check
        for i in range(9):
            if not ( ch(board.row(i)) and ch(board.col(i)) and ch(board.box(i)) ):
                return False
        return True

    def valid_move(self, idx):
        board = Sudoku(self.merge())
        r, c, b = self.coord(idx)
        ch = Sudoku.check
        if not ( ch(board.row(r)) and ch(board.col(c)) and ch(board.box(b)) ):
            return False
        return True

    def __repr__(self):
        board = Sudoku(self.merge())
        string = []
        division = 3
        spacing = 2
        space = ' ' * spacing
        line = '-' * ( ( spacing + 1 ) * ( 9 + 9 // division + 1 ) - spacing )
        for row in range(9):
            if row % division == 0: string.append(line)
            row_string = ''
            for idx, n in enumerate(board.row(row)):
                if idx % division == 0: row_string += '|' + space
                row_string += str(n)
                row_string += space
            string.append(row_string + '|' + space)
        string.append(line)
        return '\n'.join(string)

def solve(sud):
    if sud.valid():
        sud.append(1)
    else:
        sud.next()

def solve2(sud):
    if sud.valid():
        idx = len(sud.stack) - 1
        try:
            pos = sud.map[idx+1]
        except:
            import pdb; pdb.set_trace()
        # import pdb; pdb.set_trace()
        sud.append(pos[0])
    else:
        sud.next2()

def solve3(sud):
    if sud.valid():
        idx = len(sud.stack) - 1
        try:
            pos = sud.map[idx+1]
        except:
            import pdb; pdb.set_trace()
        # import pdb; pdb.set_trace()
        sud.append(pos[0])
    else:
        sud.next2()
    # update(sud)

@benchmark()
def run(sud):
    sud.logic_step()
    sud.stack.append(1)
    print(sud)
    iteration = 1
    while len(sud.stack) <= sud.limit:
        solve(sud)
        iteration += 1
        if not iteration % 100:
            update(sud)
    print(sud)
    print('SOLVED in {} iterations'.format(iteration))

@benchmark()
def run2(sud):
    print('\n'*10)
    sud.logic_step()
    sud.map = sud.poss_map()
    # print(sud)
    p = sud.map[0]
    sud.stack.append(p[0])
    iteration = 1
    while len(sud.stack) <= sud.limit:
        solve2(sud)
        iteration += 1
        if not iteration % 100:
            update(sud)
    print(sud)
    print('SOLVED in {} iterations'.format(iteration))
    print('\n' * 10)
    return sud[0] * 100 + sud[1] * 10 + sud[2]


@benchmark()
def run3(sud):
    sud.logic_step()
    sud.map = sud.poss_map()
    # print(sud)
    p = sud.map[0]
    sud.stack.append(p[0])
    iteration = 1
    while len(sud.stack) <= sud.limit:
        solve2(sud)
        iteration += 1
        if not iteration % 100:
            update(sud)
    print(sud)
    print('SOLVED in {} iterations'.format(iteration))



def clear():
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    string = (ERASE_LINE + CURSOR_UP_ONE) * 14 + '\b' * 100
    sys.stdout.write(string)
    sys.stdout.flush()


def update(sudoku):
    clear()
    print(sudoku)


def get_grids():
    with open('096.txt', 'r') as grid_file:
        return [ list(map( int, list(''.join([grid_file.readline()[:-1] for _ in range(9)])))) for line in grid_file if not line[0].isdigit()]


g = get_grids()
s = list(map(lambda lst: Sudoku(lst), g))

t = [1, 2, 3, 4]

s0 = s[5]
s1 = s[5].rotate_y()
s2 = s1.rotate_y()



# def get_grid(n):
#     with open('096.txt', 'r') as grid_file:
#         for line in grid_file:
#             if line[:-1] == 'Grid {}'.format(str(n) if n > 9 else '0' + str(n)):
#                 return list(map( int, list(''.join([grid_file.readline()[:-1] for _ in range(9)])) ))
#
# def check(grid):
#     if 0 in grid: return False
#     if Counter(grid) != Counter([x for x in range(1,10) for y in range(1, 10)]): return False
#
# # def row(n, grid):
# #     pass
#
# class Grid:
#     __slots__ = ['data', 'cols', 'rows']
#     def __init__(self, rows, cols, default_value=None, data=None):
#         self.data = data or [ [ default_value for _ in range(cols) ] for _ in range(rows) ]
#         self.cols = cols
#         self.rows = rows
#
#     def get_row(self, n):
#         first = self.cols * n
#         last = first + self.cols
#         return self.data[first:last]
#
#     def get_col(self, n):
#         return self.data[n::self.cols]
#
#     def all_rows(self):
#         for i in range(self.rows):
#             yield self.get_row(i)
#
#     def all_cols(self):
#         for i in range(self.cols):
#             yield self.get_col(i)
#
#     def get_slice(self, start, y, x):
#         result = []
#         for _ in range(y):
#             for i in range(x):
#                 result.append(self.data[start + i])
#             start += self.cols
#         return result
#
#     def get_val(self, x, y=None):
#         if y == None: x, y = x
#         return self.data[x * self.cols + y]
#
#     def set_val(self, value, x, y=None):
#         if y == None: x, y = x
#         self.data[x * self.cols + y] = value
#
#     def __str__(self):
#         string = []
#         division = 9
#         spacing = 2
#         space = ' ' * spacing
#         line = '-' * ( ( spacing + 1 ) * ( self.cols + self.cols // division + 1 ) - spacing )
#         for row in range(self.rows):
#             if row % division == 0: string.append(line)
#             row_string = ''
#             for idx, n in enumerate(self.get_row(row)):
#                 if idx % division == 0: row_string += '|' + space
#                 row_string += str(n)
#                 row_string += space
#             string.append(row_string + '|' + space)
#         string.append(line)
#         return '\n'.join(string)
#
# class Sudoku:
#     def __init__(self, data=None):
#         self.board = Grid(9, 9, 0, data=data)
#         # print(self)
#
#     def get_box(self, n):
#         start = (n // 3) * 27 + (n % 3) * 3
#         return self.board.get_slice(start, 3, 3)
#
#     def get_col(self, n):
#         return self.board.get_col(n)
#
#     def get_row(self, n):
#         return self.board.get_row(n)
#
#     @staticmethod
#     def valid(lst):
#         s = set()
#         for n in lst:
#             if n == 0: continue
#             if n in s: return False
#             s.add(n)
#         return True
#
#     def step(self):
#         state = False
#         for i in range(81):
#             c = (i // 9, i % 9)
#             if self.board.get_val(c) != 0: continue
#             p = list(self.possibilities(i))
#             if not p: return 'ERROR'
#             if len(p) == 1:
#                 state = True
#                 self.board.set_val(p[0], c)
#         # print('valid: {}'.format(self.board_valid()))
#         # print('solved: {}'.format(self.board_solved()))
#         # if state: print(self)
#         return state
#
#     def revert(self, data):
#         print(self)
#         print('REVERT')
#         self.board.data = data
#         print(self)
#
#     def guess(self):
#         saved = self.board.data[:]
#         for target_size in range(2, 9):
#             for i in range(81):
#                 p = self.possibilities(i)
#                 if len(p) == target_size:
#                     c = (i // 9, i % 9)
#                     print('P:' + str(p))
#                     for n in p:
#                         print(str(p), n)
#                         self.board.set_val(n, c)
#                         x = self.solve()
#                         print(x)
#                         if x != 'SOLVED':
#                             self.revert(saved)
#                         else:
#                             return
#                     return
#
#
#
#     def board_valid(self):
#         for col in self.board.all_cols():
#             if not Sudoku.valid(col): return False
#         for row in self.board.all_rows():
#             if not Sudoku.valid(row): return False
#         for i in range(9):
#             if not Sudoku.valid(self.get_box(i)): return False
#         return True
#
#     def board_solved(self):
#         for col in self.board.all_cols():
#             if not Sudoku.done(col): return False
#         for row in self.board.all_rows():
#             if not Sudoku.done(row): return False
#         for i in range(9):
#             if not Sudoku.done(self.get_box(i)): return False
#         return True
#
#     @staticmethod
#     def done(lst):
#         return set(lst) == {1,2,3,4,5,6,7,8,9}
#
#     @staticmethod
#     def remaining(lst):
#         return {1,2,3,4,5,6,7,8,9} - set(lst)
#
#     def solve(self):
#         # print(self)
#         def loop():
#             while True:
#                 x = self.step()
#                 if self.board_solved(): return 'SOLVED'
#                 if not x: return 'IMPASSE'
#                 if x == 'ERROR': return 'ERROR'
#                 if not self.board_valid(): return 'ERROR'
#                 if not self.step(): return 'PROGRESS'
#                 # print('SOLVED!  score: {}'.format(self.score()))
#
#         return loop()
#
#
#     def score(self):
#         return sum(self.board.get_slice(0, 1, 3))
#
#     def possibilities(self, n):
#         c = (n // 9, n % 9)
#         if self.board.get_val(c) != 0: return set()
#         box = self.get_box(3 * (n // 27) + n % 9 // 3)
#         row = self.get_row(n // 9)
#         col = self.get_col(n % 9)
#         return self.remaining(row) & self.remaining(col) & self.remaining(box)
#
#     def __str__(self):
#         return self.board.__str__()
#
#
# grids = get_grids()
# g = Sudoku(grids[2])
# #
# def run():
#     for grid in grids:
#         g = Sudoku(grid)
#         print(g.solve())

def p(sud):
    ns = Sudoku(sud.merge)
    return ns[0] * 100 + ns[1] * 10 + ns[2]
