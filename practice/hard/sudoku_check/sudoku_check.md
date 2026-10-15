# Sudoku Checker (Hard)

A solved sudoku is a 9×9 grid where every **row**, every **column** and every
**3×3 box** contains each digit 1–9 exactly once.

Here the grid is one string of 81 characters, row by row: the first 9
characters are row 0, the next 9 row 1, and so on. Rows, columns and boxes
are numbered from 0 to 8; boxes go left to right, top to bottom:

```
0 1 2
3 4 5
6 7 8
```

## Task

- Create a function `cell(grid, row, col)` that returns the character at
  that row and column
- Create a function `row_ok(grid, row)` that returns `True` if the row has
  each digit 1–9 exactly once
- Create a function `col_ok(grid, col)` — the same for a column
- Create a function `box_ok(grid, box)` — the same for a 3×3 box
- Create a function `is_solved(grid)` that returns `True` if the grid is 81
  characters long and all 9 rows, 9 columns and 9 boxes are fine

## Examples

```python
SOLVED = (
    "534678912672195348198342567859761423426853791"
    "713924856961537284287419635345286179"
)
```

| Call                                      | Returns |
|-------------------------------------------|---------|
| `cell(SOLVED, 0, 0)`                      | `"5"`   |
| `cell(SOLVED, 1, 0)`                      | `"6"`   |
| `row_ok(SOLVED, 0)`                       | `True`  |
| `box_ok(SOLVED, 4)`                       | `True`  |
| `is_solved(SOLVED)`                       | `True`  |
| `is_solved("123456789" * 9)`              | `False` |

Hints:

- the cell at `row`, `col` is at index `row * 9 + col`
- box `b` starts at row `b // 3 * 3` and column `b % 3 * 3`
- "each digit exactly once": for every digit `"1"` ... `"9"`, count how many
  times it occurs and check that the count is 1
- valid rows and columns are not enough — the boxes can still be wrong
