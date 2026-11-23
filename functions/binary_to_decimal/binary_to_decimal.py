def binary_to_decimal(binary):
    sum = 0
    for i in binary:
        sum = sum * 2 + int(i) 
    return sum    
print(binary_to_decimal("1010"))

