a = 0
b = 0

while True:
    x = int(input())
    if x == "":
        break
    if x == 1:
        b += 1
        if a < b:
            a = b
    else:
        b = 0

print("Maximum streak:", a)