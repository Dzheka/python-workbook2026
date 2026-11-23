def decimal_hex(n):
    if n == 0:
        return "0"

    digits = "0123456789ABCDEF"
    result = ""
    sign = ""

    if n < 0:
        sign = "-"
        n = -n

    while n > 0:
        remainder = n % 16
        result = digits[remainder] + result
        n //= 16
    return sign + result