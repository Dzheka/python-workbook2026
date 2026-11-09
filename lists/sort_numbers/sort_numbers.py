def sort_numbers(numbers: list[int]) -> list[int]:
    numbers2 = numbers.copy()
    return sorted(numbers2)


if __name__ == "__main__":
    # Test your function
    print(sort_numbers([5, 2, 8, 1, 9]))  # [1, 2, 5, 8, 9]
    print(sort_numbers([5, 2, 3]))        # [2, 3, 5]
