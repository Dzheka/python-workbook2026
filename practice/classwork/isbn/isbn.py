DIGITS = "0123456789"


def clean(code):
    return code.replace("-", "").replace(" ", "")


def is_valid_isbn10(code):
    code = clean(code)
    if len(code) != 10:
        return False
    for i in range(9):
        if code[i] not in DIGITS:
            return False
    if code[9] not in DIGITS and code[9] != "X":
        return False

    total = 0
    for i in range(10):
        if code[i] == "X":
            value = 10
        else:
            value = int(code[i])
        total += value * (10 - i)
    return total % 11 == 0


def isbn13_check_digit(first12):
    total = 0
    for i in range(12):
        weight = 1 if i % 2 == 0 else 3
        total += int(first12[i]) * weight
    return (10 - total % 10) % 10


def isbn10_to_13(code):
    if not is_valid_isbn10(code):
        return "invalid"
    first12 = "978" + clean(code)[:9]
    return first12 + str(isbn13_check_digit(first12))