def divisors(n: int) -> list[int]:
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    divisors.append(n)
    return divisors


if __name__ == "__main__":
    # Test your function
    print(divisors(12))   # [1, 2, 3, 4, 6, 12]
    print(divisors(7))    # [1, 7]
    print(divisors(1))    # [1]