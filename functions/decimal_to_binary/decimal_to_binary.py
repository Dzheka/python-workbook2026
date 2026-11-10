def decimal_to_binary(n):
    if n == 0:
        return '0'
    binary = ""
    while n != 0:
        if n % 2 == 0:
            binary = '0' + binary
            n = n //2
        elif n % 2 != 0:
            binary = '1' + binary
            n = n // 2
        elif n < 2:
            break
    return binary
print(decimal_to_binary(0))
