def hex_decimal(hex_str):
    hex_digits = "0123456789ABCDEF"
    decimal_value = 0

    for char in hex_str.upper():
        digit_value = hex_digits.index(char)
        decimal_value = decimal_value * 16 + digit_value

    return decimal_value