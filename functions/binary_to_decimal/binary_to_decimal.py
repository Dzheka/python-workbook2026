def binary_to_decimal(binary):
    decimal = 0
    for digit in binary:
        decimal = decimal * 2 + (1 if digit == "1" else 0)
    return decimal