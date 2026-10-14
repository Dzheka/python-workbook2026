n = int(input())

if n == 0:
    print(1)
else:
    n = abs(n)  # the minus sign is not a digit
    count = 0

    while n > 0:
        count += 1
        n //= 10

    print(count)
