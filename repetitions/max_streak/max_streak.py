current = 0
maximum = 0
while True:
    n = input()
    if n == "":
        break
    if n == "1":
        current += 1
        if current > maximum:
            maximum = current
    else:
        current = 0
print("Maximum streak:", maximum)
