def difference_of_values(lst):
    diffs = []
    for idx in range(1, len(lst)):
        diffs.append(lst[idx] - lst[idx-1])
    return diffs

def make_diffs_mtrx(lst):
    mtrx = []
    while lst:
        mtrx.append(lst)
        lst = difference_of_values(lst)
    return mtrx

def estimate_next_value(mtrx):
    for idx in reversed( range(1, len(mtrx)) ):
        mtrx[idx-1].append( mtrx[idx-1][-1] + mtrx[idx][-1])
    return mtrx[0][-1]

polynomial = lambda n: 1 - n + n**2 - n**3 + n**4 - n**5 + n**6 - n**7 + n**8 - n**9 + n**10

def sum_of_fit(polynomial):
    fit_sum = 0
    i = 2
    while True:
        mtrx = make_diffs_mtrx([ polynomial(n) for n in range(1, i) ])
        fit = estimate_next_value(mtrx)
        if fit == polynomial(i): break
        fit_sum += fit
        i += 1
    print(fit_sum)
