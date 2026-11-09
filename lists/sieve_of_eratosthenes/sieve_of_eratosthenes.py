
def sieve_of_eratosthenes(n: int) -> list[int]:
    if n < 2:
        return []

    numbers = []
    prime = [True] * (n + 1)

    prime[0] = False
    prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime[i]:
            for j in range(i*i, n + 1, i):
                prime[j] = False

    for i in range(2, n + 1):
        if prime[i]:
            numbers.append(i)

    return numbers
