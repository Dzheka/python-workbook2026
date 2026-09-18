position = input()

if (ord(position[0]) + int(position[1])) % 2 == 0:
    print("black")
else:
    print("white")
