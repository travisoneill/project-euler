from decorators import coercion, coerce_builtin

@coercion(exact={0: 100, '1': '11', 2: str, 3: lambda n: n+1, None: 5, 'none': None})
def test_exact(*args):
    return args

def test():
    state = test_exact(0) == (100,)
    print('handles simple integer case: {}'.format(state))

    state = test_exact('1') == ('11',)
    print('handles simple string case: {}'.format(state))

    state = test_exact(2) == ('2',)
    print('handles function object: {}'.format(state))

    state = test_exact(3) == (4,)
    print('handles lambda: {}'.format(state))

    state = test_exact(None) == (5,) and test_exact('none') == (None,)
    print('handles None: {}'.format(state))

    state = test_exact(10, 0, 'abc', 3, 3.5) == (10, 100 ,'abc', 4, 3.5)
    print('ignores appropriate arguments: {}'.format(state))
