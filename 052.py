def is_perm(n1, n2):
    idx = [0] * 10
    while n2 > 0 and n1 > 0:
        idx[n1 % 10] += 1
        idx[n2 % 10] -= 1
        n1 //= 10
        n2 //= 10
    return not n1 and not n2 and not [n for n in idx if n != 0]

def run(x):
    n = 1
    while True:
        for i in range(2, x+1):
            if not is_perm(n, n*i): break
        else:
            print(n)
        n += 1
