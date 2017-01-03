from collections import Counter
from functools import reduce

def decrypt(key, cipher):
    if cipher.__class__.__name__ == 'str':
        cipher = list(map(ord, list(cipher)))

    message = ''
    for i in range(len(cipher)):
        k = ord(key[i%len(key)])
        message += chr(cipher[i] ^ k)
    return message

def find_key(cipher, key_length):
    if cipher.__class__.__name__ == 'str':
        cipher = list(map(ord, list(cipher)))
    key = ''
    for i in range(key_length):
        space = Counter(cipher[i::key_length]).most_common()[0][0]
        key += chr(32 ^ space)
    return key

total = lambda string: reduce( lambda l1, l2: l1 + ord(l2), string, 0 )

def solve():
    cipher = []
    with open ('059.txt', 'r') as text:
        for line in text: cipher += list(map(int, line[:-1].split(',')))
    key = find_key(cipher, 3)
    message = decrypt(key, cipher)
    print(message)
    print(total(message))
