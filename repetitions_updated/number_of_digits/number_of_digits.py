n = int(input())

# Handle special case of 0
if n == 0:
    print(1)
else:
    # Take absolute value to handle negative numbers
    n = abs(n)
    count = 0

    while n > 0:
        count += 1
        n //= 10

    print(count)
