def to_base(n, base):
    if base < 2 or base > 36:
        return None

    if n == 0:
        return "0"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    sign = ""

    if n < 0:
        sign = "-"
        n = -n
    while n > 0:
        remainder = n % base
        result = digits[remainder] + result
        n //= base

    return sign + result