"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""
def romanToInt(s: str) -> int:
    trnslater = {
        'M': 1000,
        'CM': 900,
        'D': 500,
        'CD': 400,
        'C': 100,
        'XC': 90,
        'L': 50,
        'XL': 40,
        'X': 10,
        'IX': 9,
        'V': 5,
        'IV': 4,
        'I': 1,
    }
    num = 0
    s = s.replace('CM', 'DCCCC')
    s = s.replace('CD', 'CCCC')
    s = s.replace('XC', 'LXXXX')
    s = s.replace('XL', 'XXXX')
    s = s.replace('IX', 'VIIII')
    s = s.replace('IV', 'IIII')

    for char in s:
        if char == 'I':
            num += 1
        if char == 'V':
            num += 5
        if char == 'X':
            num += 10
        if char == 'L':
            num += 50
        if char == 'C':
            num += 100
        if char == 'D':
            num += 500
        if char == 'M':
            num += 1000

    return num

print(romanToInt("MCMXCIV"))