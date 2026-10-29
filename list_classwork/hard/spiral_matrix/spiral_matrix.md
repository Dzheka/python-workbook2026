# Spiral Matrix (Hard)

Walk a matrix (a list of rows) in a clockwise spiral: along the top row, down
the right column, back along the bottom row, up the left column, and then the
same again one layer further in.

```
1  2  3
4  5  6      ->   1 2 3 6 9 8 7 4 5
7  8  9
```

## Task

- Create a function `spiral_order(matrix)` that returns a list of all numbers
  in spiral order; the matrix does not have to be square, and an empty matrix
  `[]` gives `[]`
- Create a function `spiral_matrix(n)` that returns an `n × n` matrix filled
  with `1, 2, ..., n * n` in spiral order
- Create a function `format_matrix(matrix)` that returns the matrix as text:
  one line per row, numbers separated by single spaces, lines joined with
  `"\n"`

## Examples

| Call                                          | Returns                            |
|-----------------------------------------------|------------------------------------|
| `spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]])` | `[1, 2, 3, 6, 9, 8, 7, 4, 5]`  |
| `spiral_order([[1, 2, 3, 4], [5, 6, 7, 8]])`  | `[1, 2, 3, 4, 8, 7, 6, 5]`         |
| `spiral_matrix(3)`                            | `[[1, 2, 3], [8, 9, 4], [7, 6, 5]]`|
| `spiral_matrix(1)`                            | `[[1]]`                            |
| `format_matrix([[1, 2], [4, 3]])`             | `"1 2\n4 3"`                      |

Hint: keep four borders `top`, `bottom`, `left`, `right` and move each one
inward after walking its side. Stop as soon as `top > bottom` or
`left > right`. For `spiral_matrix`, start from `[[0] * n for _ in range(n)]`
and walk the same way, writing instead of reading.
