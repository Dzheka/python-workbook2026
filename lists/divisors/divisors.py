def divisors(n: int) -> list[int]:
    numbers = []
    for i in range(1, n + 1):
        if n % i == 0:
            numbers.append(i)
    return numbers


if __name__ == "__main__":
    # Test your function
    print(divisors(12))   # [1, 2, 3, 4, 6, 12]
    print(divisors(7))    # [1, 7]
    print(divisors(1))    # [1]
