ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(roman: str) -> int:
    s = 0
    prev = 0
    for i in roman[::-1]:
       item = ROMAN[i]
       if item >= prev:
           s += item
       else:
           s -= item
       prev = item
    return s



if __name__ == "__main__":
    print(roman_to_int("MMMCMXCIX"))  # 3999
    print(roman_to_int("LVIII"))  # 58
    print(roman_to_int("III"))  # 3