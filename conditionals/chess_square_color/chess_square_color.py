position = input()

column = position[0]
row = int(position[1])

if column == "a" or column == "c" or column == "e" or column == "g":
    if row % 2 == 1:
        print("black")
    else:
        print("white")
else:
    if row % 2 == 1:
        print("white")
    else:
        print("black")