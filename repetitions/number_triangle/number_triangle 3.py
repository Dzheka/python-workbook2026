n = int(input())

for column in range(1,n + 1):
    for row in range(1, column + 1):
        print(row, end="")
    print()
