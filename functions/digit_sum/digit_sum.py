def digit_sum(n):
    total = 0
    n = abs(n)
    while n != 0:
        total += n % 10
        n = n // 10
    return total