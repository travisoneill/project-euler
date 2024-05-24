import math
from benchmark import benchmark


def n2b(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def test(n, v=False):
    count = 0
    for i in range(1, 3**(math.ceil(math.log2(n))+1)):
        dig = n2b(i, 3)
        x = 0
        pow = 1
        for i in reversed(range(len(dig))):
            x += dig[i] * pow
            pow *= 2
        if x == n:
            count += 1
            if v:
                print(dig)
    return count


def test2(n, v=False):
    count = 0
    for i in range(1, 3**(math.ceil(math.log2(n))+1)):
        dig = n2b(i, 3)
        x = 0
        pow = 2**(len(dig)-1)
        for i in range(len(dig)):
            x += dig[i] * pow
            pow //= 2
            if x > n:
                break
        if x == n:
            count += 1
            if v:
                print(dig)
    return count



    # arr = [0 for _ in range(10)]

# 1
# 2 1
# 3 2  3 1
# 4 3  5 2  5 3  4 1
# 5 4  7 3  8 5  7 2  7  5  8 3  7  4  5 1
# 6 5  9 4 11 7 10 3 11  8 13 5 12  7  9 2  9  7 12 5 13  8 11 3 10  7 11 4  9 5  6 1
# 7 6 11 5 14 9 13 4 15 11 18 7 17 10 13 3 14 11 19 8 21 13 18 5 17 12 19 7 16 9 11 2 11 9 16 7 19 12 17 5 18 13 21 8 19 11 14 3 13 10 17 7 18 11 15 4 13 9 14 5 11 6 7 1


# 4   - {val: 3, ser: 0, nxt_ser: 2}
# 6   - {val: 3, ser: 2, nxt_ser: 3}
# 10  - {val: 5, ser: 2, nxt_ser: 3}
# 18  - {val: 7, ser: 2, nxt_ser: 3}
# 34  - {val: 9, ser: 2, nxt_ser: 3}
# 66  - {val: 11, ser: 2, nxt_ser: 3}
# 124 - {val: 11, ser: 3, nxt_ser: 11}
# 188 - {val: 14, ser: 3, nxt_ser: 11}

# 1000
# ref = 512 + 255 = 767
# 534 = 512 + 22
# 256 + 22
# 128 + 22
# 64 + 22
# 32 + 22 = 54
# ref = 32 + 15 = 47
# 40 = 32 + 8
# 16 + 8
# ref = 23
# 22 = 16 + 6
# 8 + 6 = 14
# ref = 8 + 3 = 11
# 8


# 8 - 4
# 14 - 4 (3)
# 22 - 7 - flip - (4 ser)
# 24 - 7
# 40 - 11 - flip over (32+15)
# 54 - 11 - 7 ser (32 + 22)
# 86 - 18 (64 + 22)
# 150 - 25 (128 + 22)
# 278 - 32 (256 + 22)
# 534 - 39 (512 + 22)


def get_path(n):
    out = []
    while True:
        pow = int(math.log2(n))
        msb = 2**pow
        if n == msb:
            out.append((0, 'start', n))
            break
        pivot = msb + 2**(pow-1) - 1
        if n > pivot:
            diff = n - pivot
            out.append((pivot - diff, 'flip', n))
            n = pivot - diff
        elif n < pivot:
            diff = n - msb
            out.append((2**(pow-1) + diff, 'step', n))
            n = 2**(pow-1) + diff
    return out

@benchmark()
def traverse(n):
    if math.log2(n+1) % 1 == 0:
        return 1
    path = list(reversed(get_path(n)))
    temp_val = 0
    ser = 0
    nxt_ser = 0
    for curr, op, nxt in path:
        if op == 'start':
            pow = int(math.log2(nxt))
            temp_val = pow + 1
            nxt_ser = pow
        elif op == 'step':
            nxt_ser = temp_val
            temp_val += ser
        elif op == 'flip':
            ser = nxt_ser
            nxt_ser = temp_val
        # print(nxt, temp_val, ser, nxt_ser)
    return temp_val



# 113 

# 64 + 31 = 95

# 64 + 13
# 32 + 13
# 16 + 13

# 29 > 16 + 7
# 23
# 17

# 16 + 1
# 8 + 1
# 4 + 1
# 2 + 1



# 32 4
# 32 2 2
# 32 2 1 1
# 16 16 4
# 16 16 2 2
# 16 16 2 1 1
# 16 8 8 4
# 16 8 8 2 2
# 16 8 8 2 1 1
# 16 8 4 4 2 2
# 16 8 4 4 2 1 1




# 64 32 4
# 64 32 2 2

# 512 256 128 64 32 8
# 512 256 128 64 32 4 4
# 512 256 128 64 32 4 2 2
# 512 256 128 64 32 4 2 1 1

# 512 256 128 64 16 16 8
# 512 256 128 64 16 16 4 4
# 512 256 128 64 16 16 4 2 2
# 512 256 128 64 16 16 4 2 1 1

# 512 256 128 64 16  8 8 4 4
# 512 256 128 64 16  8 4 2 2
# 512 256 128 64 16 16 4 2 1 1

# 512 256 128 64 16 8 8 4 4
# 512 256 128 64 16 8 8 4 2 2
# 512 256 128 64 16 8 8 4 2 1 1

# 512 256 128 32 32 16 8 8 4 4
# 512 256 128 32 32 16 8 8 4 2 2
# 512 256 128 32 32 16 8 8 4 2 1 1

# 512 256 64 64 32 32 16 8 8 4 4
# 512 256 64 64 32 32 16 8 8 4 2 2
# 512 256 64 64 32 32 16 8 8 4 2 1 1

# 512 128 128 64 64 32 32 16 8 8 4 4
# 512 128 128 64 64 32 32 16 8 8 4 2 2
# 512 128 128 64 64 32 32 16 8 8 4 2 1 

# 256 256 128 128 64 64 32 32 16 8 8 4 4
# 256 256 128 128 64 64 32 32 16 8 8 4 2 2
# 256 256 128 128 64 64 32 32 16 8 8 4 2 1 1


# 64 32 4
# 512 256 128 64 32 8
# 8192 1024 512 256 16
# 65536 32768 1024 512 128 32

# 83 78 74 72 71 68 66 64 60 58 57 52 50 40 38 35 30 27 25



