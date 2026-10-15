def digit_sum(n):
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + digit_sum(n // 10)