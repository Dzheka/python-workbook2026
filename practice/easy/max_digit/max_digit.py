def max_digit(n):
    n = abs(n)
    l = n % 10
    while n > 0:
        l = max(l, n % 10)
        n //= 10
    return l


def min_digit(n):
    n = abs(n)
    s = n % 10
    while n > 0:
        s = min(s, n % 10)
        n //= 10
    return s


def digit_range(n):
    return max_digit(n) - min_digit(n)