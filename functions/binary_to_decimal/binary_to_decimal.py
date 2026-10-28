def binary_to_decimal(binary):
    decimal = 0
    for bit in binary:
        decimal = decimal * 2 + (1 if bit == "1" else 0)
    return decimal