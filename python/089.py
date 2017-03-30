from benchmark import benchmark

def optimize(roman):
    roman = roman.replace('IIIII', 'V')
    roman = roman.replace('VV', 'X')
    roman = roman.replace('XXXXX', 'L')
    roman = roman.replace('LL', 'C')
    roman = roman.replace('CCCCC', 'D')
    roman = roman.replace('DD', 'M')
    roman = roman.replace('DCCCC', 'CM')
    roman = roman.replace('CCCC', 'CD')
    roman = roman.replace('LXXXX', 'XC')
    roman = roman.replace('XXXX', 'XL')
    roman = roman.replace('VIIII', 'IX')
    roman = roman.replace('IIII', 'IV')
    return roman

@benchmark()
def run():
    with open('089.txt', 'r') as numerals:
        savings = 0
        for line in numerals:
            rn = line[:-1]
            opt = optimize(rn)
            diff = len(rn) - len(opt)
            savings += diff
        return savings
