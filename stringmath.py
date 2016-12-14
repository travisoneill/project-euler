def add_str(str1, str2):
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
    from random import randint
    print('adds positive numbers:')
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
