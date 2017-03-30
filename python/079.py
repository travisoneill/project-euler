from benchmark import benchmark

def get_password_data(filename):
    nums = set()
    combos = set()
    with open(filename, 'r') as numbers:
        for line in numbers:
            tup = tuple(map(int, tuple(line[:-1])))
            combos.add( tup[:2])
            combos.add( tup[1:] )
            combos.add( (tup[0], tup[2]) )
            nums = nums | set(tup)
    return { 'nums_used': nums, 'combinations': combos}

def tup_insert(tu, idx, val):
    return tu[:idx] + (val,) + tu[idx:]

def tup_swap(tu, i, j):
    i, j = sorted([i, j])
    return tu[:i] + (tu[j],) + tu[i+1:j] + (tu[i],) + tu[j+1:]

def int_from_tup(tup):
    integer = 0
    for d in tup:
        integer *= 10
        integer += d
    return integer

get_idx = lambda tup, pw: tuple( map( lambda n: pw.index(n), tup ) )

@benchmark()
def run():
    data = get_password_data('079.txt')
    pw = tuple(data['nums_used'])
    while True:
        for c in data['combinations']:
            idx = get_idx(c, pw)
            if idx[0] > idx[1]:
                pw = tup_swap(pw, *idx)
                break
        else:
            break
    return int_from_tup(pw)

# CLI Shortcuts
ti = tup_insert
ts = tup_swap
gi = get_idx
gp = get_password_data
