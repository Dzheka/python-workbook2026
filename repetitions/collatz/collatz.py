n = int(input())

while n > 0:
    print(n)

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        print(n)

    n = int(input())
