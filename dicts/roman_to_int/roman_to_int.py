ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(roman: str):
    t = 0

    for i in range(len(roman)):
        a = ROMAN[roman[i]]

        if i + 1 < len(roman) and a < ROMAN[roman[i + 1]]:
            t -= a
        else:
            t += a

    return t