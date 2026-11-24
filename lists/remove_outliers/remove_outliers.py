def remove_outliers(numbers: list[int]) -> list[int]:
    minimum = min(numbers)
    maximum = max(numbers)
    numbers.remove(maximum)
    numbers.remove(minimum)
    return numbers

if __name__ == "__main__":
    # Test your function
    print(remove_outliers([2, 3, 5, 7, 11]))    # [3, 5, 7]
    print(remove_outliers([10, 5, 8, 3]))       # [5, 8]
    print(remove_outliers([3, 7, 1, 9, 4, 6]))  # [3, 7, 4, 6]