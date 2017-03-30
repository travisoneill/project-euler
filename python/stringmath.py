def add_str(str1, str2):
    if '.' in str1 + str2:
        return add_flt(str1, str2)
    else:
        return add_int(str1, str2)

def add_flt(str1, str2):
    if '.' not in str1: str1 += '.'
    if '.' not in str2: str2 += '.'
    flt1, flt2 = str1.split('.'), str2.split('.')
    integers = pad(flt1[0], flt2[0], direction='left')
    decimals = pad(flt1[1], flt2[1], direction='right')
    position = -len(decimals[0])
    result = add_int(integers[0] + decimals[0], integers[1] + decimals[1])
    return result[:position] + '.' + result[position:]

def pad(*args, direction=''):
    longest = 'n'
    padded = []
    for string in args:
        if len(string) > len(longest): longest = string
    for string in args:
        diff = len(longest) - len(string)
        if direction == 'left': padded.append(diff*'0' + string)
        if direction == 'right': padded.append(string+ diff*'0')
    return tuple(padded)


def add_int(str1, str2):
    '''Adds 2 strings as if they were integers.'''
    length_diff = abs( len(str1) - len(str2) )
    if len(str2) > len(str1): str1, str2 = str2, str1
    str2 = ('0' * length_diff) + str2
    result = ''
    carry = 0
    for idx in reversed(range(len(str1))):
        d1 = str1[idx:idx+1] or 0
        d2 = str2[idx:idx+1] or 0
        sm = int(d1) + int(d2) + carry
        digit = sm % 10
        result = str(digit) + result
        carry = sm // 10
    if carry > 0: result = str(carry) + result
    return result

def test():
    from random import randint, random
    random_float = lambda: random() * 10

    print('adds positive integers:')
    for _ in range(10000):
        n1 = randint(0, 1000000)
        n2 = randint(0, 1000000)
        s1 = str(n1)
        s2 = str(n2)
        if n1+n2 != int(add_str(s1, s2)):
            print(False)
            print('FAILURE: ', n1, n2)
            break
    else:
        print(True)

    # print('adds positive floats:')
    # for _ in range(10000):
    #     n1 = random_float()
    #     n2 = random_float()
    #     s1 = str(n1)
    #     s2 = str(n2)
    #     if str(n1+n2) != add_str(s1, s2):
    #         print(False)
    #         print('FAILURE: ', n1, n2)
    #         break
    # else:
    #     print(True)
    #
    # print('adds positive floats to integers:')
    # for _ in range(10000):
    #     n1 = random_float()
    #     n2 = randint(0, 1000000)
    #     s1 = str(n1)
    #     s2 = str(n2)
    #     if str(n1+n2) != add_str(s1, s2):
    #         print(False)
    #         print('FAILURE: ', n1, n2)
    #         break
    # else:
    #     print(True)
