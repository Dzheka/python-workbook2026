numerals = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
by_value = {v: k for k, v in numerals.items()}

def from_roman(n):
    result = 0
    prev = 0
    for i in reversed(n):
        if i in numerals.keys():
            value = numerals[i]
            if value < prev:
                result -= value
            else:
                result+= value
            prev = value
    return result

values = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
    (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
    (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
    (1, 'I'),
]

def to_roman(n):
   result = ''
   for value, symbol in values:
       while n >= value:
           result += symbol
           n-= value
   return result

def is_roman(text):
    for i in text:
        if i not in 'MDCLXVI':
            return False
    n = from_roman(text)
    if n < 1 and n > 3999:
        return False
    return to_roman(n) == text