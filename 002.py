def fib(n):
    result = 0
    a, b = 0, 1
    while(a < n):
        if a % 2 == 0:
            result += a
        a, b = b, a+b
    print(result)

fib(4000000)
