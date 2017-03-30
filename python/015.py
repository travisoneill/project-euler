from math import factorial

# ONE LINER O(1)
problem15 = lambda rows, columns: factorial(rows + columns) // ( factorial(rows) * factorial(columns) )

# O(R*C)
def lattice_paths(rows, columns):
    row = [0] * columns
    row[0] = 1
    for _ in range(rows):
        row = add_across(row)
    return row[-1]

def add_across(arr):
    for i in range(1, len(arr)):
        arr[i] += arr[i-1]
    return arr
