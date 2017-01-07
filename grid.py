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

    def __str__(self, division=0, spacing=1):
        string = []
        division = 0
        spacing = 1
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
