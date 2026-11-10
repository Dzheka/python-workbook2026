def is_perfect(n: int):
    if n <= 1:
        return False

    a = 0

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            a += i

    return a == n