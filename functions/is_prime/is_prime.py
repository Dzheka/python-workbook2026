def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n > 0:
        for i in range(2, n):
            if n % i == 0:
                return False
    else:
        for i in range(2, n, -1):
            if n % i == 0:
                return False
    return True