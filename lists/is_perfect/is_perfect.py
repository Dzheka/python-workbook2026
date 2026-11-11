def divisors(n: int) -> list[int]:
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors



def is_perfect(n: int) -> bool:
    return True if sum(divisors(n)) == n else False


if __name__ == "__main__":
    # Test your function
    print(is_perfect(6))  # True (1 + 2 + 3 = 6)
    print(is_perfect(28))  # True (1 + 2 + 4 + 7 + 14 = 28)
    print(is_perfect(12))  # False