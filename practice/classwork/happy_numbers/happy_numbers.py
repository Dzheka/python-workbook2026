def square_digit_sum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit * digit
        n //= 10
    return total


def is_happy(n):
    while n != 1 and n != 4:
        n = square_digit_sum(n)
    return n == 1


def count_happy(start, end):
    count = 0
    for n in range(start, end + 1):
        if is_happy(n):
            count += 1
    return count


def nth_happy(k):
    n = 0
    found = 0
    while found < k:
        n += 1
        if is_happy(n):
            found += 1
    return n
