s = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
def roman_to_int(x):
    a=0
    b=0
    for i in reversed(x):
        c = s[i]
        if c<b:
            a=a-c
        else:
            a=a+c
        b=c
    return a
print(roman_to_int("III"))     # 3
print(roman_to_int("IV"))      # 4
print(roman_to_int("IX"))      # 9
print(roman_to_int("LVIII"))   # 58
print(roman_to_int("MCMXCIV")) # 1994
print(roman_to_int("I"))       # 1
print(roman_to_int("XIV"))     # 14