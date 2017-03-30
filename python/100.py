from math import sqrt

def run(limit):
    total = 2
    ratio = None
    results = []
    while total < limit:
        blue = int(total * (sqrt(2) / 2)) + 1
        if blue * (blue - 1) * 2 == total * (total - 1):
            print(blue, total - blue, total)
            results.append((blue, total))
            if total > 100000:
                ratio = results[-1][1] / results[-2][1]
                total = int(total * ratio) - 100000
        total += 1
