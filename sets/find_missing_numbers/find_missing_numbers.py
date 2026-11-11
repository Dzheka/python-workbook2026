def find_missing(numbers: list, n: int) -> list:
    result = []
    numbers = set(numbers)
    for i in range(1, n + 1):
        if i not in numbers:
            result.append(i)
    return result


if __name__ == "__main__":
    print(find_missing([1, 2, 4, 6], 6))  # [3, 5]
    print(find_missing([2, 3, 7, 8], 10))  # [1, 4, 5, 6, 9, 10]
    print(find_missing([1, 2, 3], 3))  # []
    print(find_missing([], 5))  # [1, 2, 3, 4, 5]
    print(find_missing([1, 1, 2, 2], 4))  # [3, 4]