from benchmark import benchmark

def reverse_digits_of(n):
    x = 0
    while True:
        x += n % 10
        n //= 10
        if not n:
            return x
        x *= 10

r = reverse_digits_of

def is_lychrel(n):
    n += reverse_digits_of(n)
    for _ in range(50):
        rev = reverse_digits_of(n)
        if n == rev:
            return False
        n += rev
    return True

l = is_lychrel

@benchmark()
def run(n):
    return len([ x for x in range(n) if is_lychrel(x) ])
