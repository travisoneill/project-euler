def triangular(limit):
    '''Generates triangular numbers up to limit.  Pass 'None' as argument to infinite loop'''
    if not limit: print('WARNING: Running in infinite loop mode')
    tri = lambda n: (n**2 + n) // 2
    i = 1
    while not limit or i < limit + 1:
        yield tri(i)
        i += 1
