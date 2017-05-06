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
        i = pos.index(num)
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

def p(sud):
    ns = Sudoku(sud.merge)
    return ns[0] * 100 + ns[1] * 10 + ns[2]
