position = input().lower()
letter = position[0]
number = int(position[1])

if (ord(letter) + number) % 2 == 0:
    print("black")
else:
    print("white")
