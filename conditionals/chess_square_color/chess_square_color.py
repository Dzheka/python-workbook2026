square = input()

column = ord(square[0]) - ord("a") + 1
row = int(square[1])

if (column + row) % 2 == 0:
    print("black")
else:
    print("white")