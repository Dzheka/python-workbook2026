n = input()
result = 0
for digit in n:
    result = result * 2 + int(digit)
print("The decimal equivalent is", result)