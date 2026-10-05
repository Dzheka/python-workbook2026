n = int(input())

for i in range(1, n + 1):
    # Print leading spaces
    print(" " * (n - i), end="")

    # Print ascending numbers
    for j in range(1, i + 1):
        print(j, end="")

    # Print descending numbers
    for j in range(i - 1, 0, -1):
        print(j, end="")

    print()
