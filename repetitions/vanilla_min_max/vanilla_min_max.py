min = False
max = False
while True:
    i = input()
    if i == '':
        break
    i = int(i)
    if not min:
        min = i
        max = i
    if i > max:
        max = i
    if i < min:
        min = i
print(f"Minimum: {min}")
print(f"Maximum: {max}")
