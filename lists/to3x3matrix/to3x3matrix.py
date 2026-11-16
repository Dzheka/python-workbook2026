def to3x3matrix(string: str) -> list[list[int]]:
    numbers = [int(num) for num in string.split()]
    return [numbers[i:i + 3] for i in range(0, 9, 3)]
