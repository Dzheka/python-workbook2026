def sieve_of_eratosthenes(n: int) -> list[int]:
    if n < 2:
        return []

    a = [True] * (n + 1)
    a[0] = a[1] = False

    p = 2
    while p * p <= n:
        if a[p]:
            for j in range(p * p, n + 1, p):
                a[j] = False
        p += 1

    return [i for i in range(2, n + 1) if a[i]]
