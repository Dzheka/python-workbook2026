def hex_decimal(hex_str):
    digits = "0123456789ABCDEF"
    result = 0

    for char in hex_str.upper():
        value = digits.index(char)
        result = result * 16 + value

    return result
print(hex_decimal("A"))