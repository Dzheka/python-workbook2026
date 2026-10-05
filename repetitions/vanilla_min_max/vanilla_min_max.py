max = 0
min = 0

while True:
    a = int(input())
    if a == '':
        break
    if not min:
        min = a
        max = a
    if a > max:
        max = a
    if a < min:
        min = a
print(f"Minimum: {min}")
print(f"Maximum: {max}")