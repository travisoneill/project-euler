def factors(n):
    count = 0
    for i in range(100, 1000):
        if n%i == 0 and n//i > 99 and n//i < 1000:
            count += 1
        if count > 1:
            return True
    return False

def pal(n):
    return n*1000 + (n%10 * 100) + (n//10 % 10)*10 + (n//100 % 10)

for n in reversed(range(1000)):
    if(factors(pal(n))):
        print(pal(n))
        break
