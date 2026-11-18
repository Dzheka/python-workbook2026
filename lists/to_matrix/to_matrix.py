def to_matrix(numbers: list[int], rows: int, cols: int):
    a = []

    for i in range(rows):
        b = i * cols
        a.append(numbers[b:b + cols])

    return a
