def remove_outliers(numbers: list[int]):
    a = numbers.copy()
    x = min(numbers)
    y = max(numbers)

    a.remove(x)
    a.remove(y)

    return a