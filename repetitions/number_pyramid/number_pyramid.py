a = int(input())
for i in range(1, a + 1):
    print(" " * (a - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()