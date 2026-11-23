ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}



def roman_to_int(roman: str) -> int:
    total = 0

    for i, char in enumerate(roman):
        value = ROMAN[char]

        if i < len(roman) - 1 and value < ROMAN[roman[i + 1]]:
            total -= value
        else:
            total += value

    return total