from operator import mul, add, sub, truediv
from itertools import combinations_with_replacement, permutations, combinations
from benchmark import benchmark

# [(3 + 2) * 4 / 5] -> [5 * 4 / 5] -> [20 / 5] -> [4]
# [(3 + 2) * (4 / 5)] -> [5 * 4 / 5] -> [5 * 0.8] -> [4]
# [3 + 2 * 4 / 5] -> [3 + 8 / 5] -> [3 + 1.6] -> [4.6]
# [(3 + 2 * 4) / 5] -> [3 + 8 / 5] -> [11 / 5] -> [2.2]
# [3 + 2 * (4 / 5)] -> [3 + 2 * 0.8] -> [3 + 1.6] -> [4.6]
# [(3 + 2) * (4 / 5)] -> [3 + 2 * 0.8] -> [5 * 0.8] -> [4]



parens = [
    {},
    {0: '(', 1: ')'},
    {0: '(', 1: '(', 2: '))'},
    {0: '((', 1: ')', 2: ')'},
    {0: '(', 1: ')', 2: '(', 3: ')'},
    {0: '(', 2: ')'},
    {1: '(', 2: ')'},
    {1: '(', 2: '(', 3: '))'},
    {1: '((', 2: ')', 3: ')'},
    {1: '(', 3: ')'},
    {2: '(', 3: ')'},
]

operators = ['+', '-', '*', '/']
dig = [d for d in range(1, 10)]


def apply_parens_and_operators(tup, parens, operators=None):
    n = []
    operators = operators or ('+', '*', '+')
    operators += ('',)
    for i in range(len(tup)):
        p = parens.get(i)
        if p and p[0] == '(':
            n.append(p)
        n.append(str(tup[i]))
        if p and p[0] == ')':
            n.append(p)
        n.append(operators[i])
    return ' '.join(n).strip(' ')

t1 = (1,2,3,4)

def all_options(tup):
    st = set()
    for par in parens:
        for comb in combinations_with_replacement(operators, 3):
            for opp in permutations(comb):
                s = apply_parens_and_operators(tup, par, opp)
                try:
                    num = eval(s)
                    # print(s, num)
                    if num > 0 and num % 1 == 0:
                        st.add(num)
                except:
                    continue
    return st

# @benchmark()
def single_comb(tup):
    st = set()
    for perm in permutations(tup):
        for n in all_options(perm):
            st.add(n)
    return st

def first_not_in(sett):
    i = 1
    while True:
        if i not in sett:
            break
        i += 1
    return i

def _eval_step(string):
    ops = {'/': truediv, '*': mul, '+': add, '-': sub}
    arr = string.strip('()').split(' ')
    intermediate = [int(arr[0])]
    idx = 1
    operator = None

    while idx < len(arr):
        token = arr[idx]
        if token.isdigit():
            token = int(token)
            if operator in ('*', '/'):
                n1 = intermediate.pop()
                n2 = token
                intermediate.append(ops[operator](n1, n2))
            else:
                intermediate.append(operator)
                intermediate.append(token)
        else:
            operator = token
        idx += 1
    print(intermediate)

    idx = 1
    val = intermediate[0]
    while idx < len(intermediate):
        token = intermediate[idx]
        if token in ('+', '-'):
            nxt = intermediate[idx+1]
            print(val, nxt)
            val = ops[token](val, nxt)
        idx += 1
    return val



ap = apply_parens_and_operators
c = combinations_with_replacement
ao = all_options
fni = first_not_in

@benchmark()
def run():
    digits = [d for d in range(1, 10)]
    for c in combinations(digits, 4):
        s = single_comb(c)
        print(fni(s), c)



a = (3, '+', 2, '*', 4, '/', 5)
operations = {'/': truediv, '*': mul, '+': add, '-': sub}
def eval_step(tup, idx):
    i = idx * 2 + 1
    result = operations[tup[i]](tup[i - 1], tup[i + 1])
    return tup[:i-1] + (result,) + (tup[i+2:])

def evaluate(tup, order):
    for idx in order:
        try:
            tup = eval_step(tup, idx)
        except ZeroDivisionError:
            return 0
    return tup[0]

all_possible_orders = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 0), (2, 0, 0), (2, 1, 0)]
def evaluate_all(tup):
    result = set()
    for order in all_possible_orders:
        result.add(evaluate(tup, order))
    return result

def merge(t1, t2):
    return(t1[0], t2[0], t1[1], t2[1], t1[2], t2[2], t1[3])

@benchmark()
def run2():
    max_fni = 0
    digits = [d for d in range(1, 10)]
    operators = ('+', '-', '*', '/')
    for comb in combinations(digits, 4):
        all_results = set()
        for perm in permutations(comb):
            for ops in combinations_with_replacement(operators, 3):
                for o in permutations(ops):
                    tup = merge(perm, o)
                    for r in evaluate_all(tup):
                        all_results.add(r)
        first = first_not_in(all_results)
        if first > max_fni:
            max_fni = first
            print(comb, first)
