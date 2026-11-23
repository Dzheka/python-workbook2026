def luhn_sum(number):
    total = 0
    for i, ch in enumerate(reversed(number)):
        d = int(ch)
        if i % 2 == 1:
            d *= 2
            if d > 9:
                d -= 9
        total += d
    return total


def is_valid_card(number):
    if len(number) < 2:
        return False
    for ch in number:
        if ch not in "0123456789":
            return False
    return luhn_sum(number) % 10 == 0


def check_digit(partial):
    for d in range(10):
        if luhn_sum(partial + str(d)) % 10 == 0:
            return d


def mask(number):
    if len(number) <= 4:
        return number
    return "*" * (len(number) - 4) + number[-4:]