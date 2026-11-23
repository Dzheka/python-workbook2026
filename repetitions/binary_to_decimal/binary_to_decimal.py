binary = input()

result = 0

for digit in binary:
    result = result * 2 + int(digit)

print(result)
