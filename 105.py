from itertools import combinations

def is_special(sett):
    if 0 in sett: return False
    lst = sorted(sett)
    ratio = lst[-1] / lst[0]
    for i in range(len(lst) // 2):
        if( sum(lst[:i+2]) <= sum(lst[-(i+1):]) ):
            return False
    for i in range(2, len(lst) // 2 + 1):
        seen = {}
        for tup in combinations(sett, i):
            if seen.get(sum(tup)): return False
            seen[sum(tup)] = True
    return True

with open('105.txt', 'r') as sets:
    count = 0
    for line in sets:
        sett = set( map(int, line[:-1].split(',')) )
        if is_special(sett): count += sum(sett)
    print(count)
