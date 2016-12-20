def digital_sum(n):
    d_sum = 0
    while n > 0:
        d_sum += n%10
        n //= 10
    return d_sum

def run(n):
    max_digital_sum = 0
    for a in range(n):
        for b in range(n):
            max_digital_sum = max(max_digital_sum, digital_sum(a**b))
    print(max_digital_sum)                
