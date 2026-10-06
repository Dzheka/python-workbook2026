import string
def to_base(n, base):
    if not (2 <= base <= 36):
        raise ValueError("Base must be between 2 and 36")

    if n == 0:
        return "0"

    is_negative = n < 0
    n = abs(n)

    digits = string.digits + string.ascii_uppercase
    result = []

    while n > 0:
        remainder = n % base
        result.append(digits[remainder])
        n //= base

    if is_negative:
        result.append("-")

    return "".join(reversed(result))