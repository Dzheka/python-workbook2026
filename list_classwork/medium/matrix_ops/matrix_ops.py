def row_sums(matrix):
    result = []

    for row in matrix:
        total = 0
        for num in row:
            total += num
        result.append(total)

    return result


def col_sums(matrix):
    result = []

    for c in range(len(matrix[0])):
        total = 0
        for r in range(len(matrix)):
            total += matrix[r][c]
        result.append(total)

    return result


def transpose(matrix):
    result = []

    for c in range(len(matrix[0])):
        new_row = []
        for r in range(len(matrix)):
            new_row.append(matrix[r][c])
        result.append(new_row)

    return result


def diagonal_sum(matrix):
    total = 0

    for i in range(len(matrix)):
        total += matrix[i][i]

    return total
