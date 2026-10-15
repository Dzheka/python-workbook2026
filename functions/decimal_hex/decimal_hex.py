def decimal_hex(n):
    if n == 0:
        return "0"

    is_negative = n < 0
    n = abs(n)
    hex_chars = "0123456789ABCDEF"
    digits = []

    while n > 0:
        remainder = n % 16
        digits.append(hex_chars[remainder])
        n //= 16

    if is_negative:
        digits.append("-")

    return "".join(reversed(digits))