from time import time
from platform import platform, python_version

def benchmark(iterations=1):
    def wrapper(func):
        def wrapped_func(*args, **kwargs):
            t0 = time()
            for _ in range(iterations):
                val = func(*args, **kwargs)
            t1 = time()
            print( 'run time: {} ms'.format( (t1 - t0) // 0.000001 / 1000 ) )
            print( 'system: {}'.format( platform() ) )
            print( 'python version: {}'.format( python_version() ) )
            return val

        return wrapped_func

    return wrapper

@benchmark(2)
def test(*args):
    print(args)
