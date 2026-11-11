def sieve_of_eratosthenes(n: int) -> list[int]:
    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
        if is_prime:
            primes.append(i)
    return primes



if __name__ == "__main__":
    # Test your function
    print(sieve_of_eratosthenes(20))  # [2, 3, 5, 7, 11, 13, 17, 19]
    print(sieve_of_eratosthenes(10))  # [2, 3, 5, 7]