def number_of_digits(n):
    if n == 0:
        return 1

    n = abs(n)
    count = 0
    while n > 0:
        count += 1
        n //= 10

    return count