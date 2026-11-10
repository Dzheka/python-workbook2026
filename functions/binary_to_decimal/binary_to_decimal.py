def binary_to_decimal(binary):
    decimal = 0
    binary = binary[::-1]
    for i in range(len(binary)):
        decimal += int(binary[i]) * 2 ** i
    return decimal
print(binary_to_decimal("1010"))
