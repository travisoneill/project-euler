from collections import Counter, defaultdict

def run(n):
    cache = defaultdict(list)
    i = 1
    while True:
        cube = i**3
        string = str(sorted(Counter(str(i**3)).items()))
        cache[string].append(i)
        if len(cache[string]) == n:
            print(cache[string])
            return min(cache[string])**3
        i += 1
