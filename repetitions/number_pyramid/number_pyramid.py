n=int(input())
for row in range(1, n + 1 ):
    for i in range(1, n - row + 1):
        print(end=" ")
    for i in range(1, row + 1):
        print(i, end='')
    for i in range(row - 1, 0, -1):
        print(i, end="")
    print(end='\n')