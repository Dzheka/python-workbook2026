def  decimal_to_binary(n):
    if n == 0:
        return "0"
    
    sum = ""
    
    while n > 0:
        digit = n % 2
        sum = str(digit) + sum
        n = n // 2
    return sum
print(decimal_to_binary(10))    