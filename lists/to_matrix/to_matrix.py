def to_matrix(numbers: list[int], rows: int, cols: int) -> list[list[int]]:
    matrix = []
    for r in range(rows):
        start = r * cols
        end = start + cols
        matrix.append(numbers[start:end])
    return matrix