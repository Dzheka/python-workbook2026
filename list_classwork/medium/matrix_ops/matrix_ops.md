# Matrix Operations (Medium)

A matrix is a list of rows, and every row is a list of numbers of the same
length:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
]
```

## Task

- Create a function `row_sums(matrix)` that returns a list with the sum of
  every row
- Create a function `col_sums(matrix)` that returns a list with the sum of
  every column
- Create a function `transpose(matrix)` that returns a **new** matrix whose
  rows are the columns of the original
- Create a function `diagonal_sum(matrix)` that returns the sum of the main
  diagonal (top-left to bottom-right) of a **square** matrix

You may assume the matrix has at least one row and one column. The original
matrix must not change.

## Examples

| Call                                      | Returns                      |
|-------------------------------------------|------------------------------|
| `row_sums([[1, 2, 3], [4, 5, 6]])`        | `[6, 15]`                    |
| `col_sums([[1, 2, 3], [4, 5, 6]])`        | `[5, 7, 9]`                  |
| `transpose([[1, 2, 3], [4, 5, 6]])`       | `[[1, 4], [2, 5], [3, 6]]`   |
| `transpose([[7]])`                        | `[[7]]`                      |
| `diagonal_sum([[1, 2], [3, 4]])`          | `5`                          |

Hint: `len(matrix)` is the number of rows and `len(matrix[0])` the number of
columns. `matrix[r][c]` is the number in row `r`, column `c`.
