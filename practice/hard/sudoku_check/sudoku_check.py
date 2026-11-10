DIGITS = "123456789"


def cell(grid, row, col):
    return grid[row * 9 + col]


def _all_digits_once(values):
    for d in DIGITS:
        if values.count(d) != 1:
            return False
    return True


def row_ok(grid, row):
    values = [cell(grid, row, c) for c in range(9)]
    return _all_digits_once(values)


def col_ok(grid, col):
    values = [cell(grid, r, col) for r in range(9)]
    return _all_digits_once(values)


def box_ok(grid, box):
    start_row = box // 3 * 3
    start_col = box % 3 * 3
    values = []
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            values.append(cell(grid, r, c))
    return _all_digits_once(values)


def is_solved(grid):
    if len(grid) != 81:
        return False
    for i in range(9):
        if not (row_ok(grid, i) and col_ok(grid, i) and box_ok(grid, i)):
            return False
    return True