# Sudoku Check (Medium)

A row of a sudoku has 9 cells. A filled row holds every number from `1` to
`9` exactly once. An empty cell is written as `0`.

## Task

- Create a function `missing(row)` that returns the numbers from 1 to 9 that
  are not in the row, sorted from smallest to largest
- Create a function `valid_group(row)` that returns `True` only if the row has
  exactly 9 cells and holds every number from 1 to 9
- Create a function `has_conflict(row)` that returns `True` if some number
  other than `0` appears more than once

## Examples

| Call                                                | Returns     |
|-----------------------------------------------------|-------------|
| `missing([5, 3, 0, 0, 7, 0, 0, 0, 0])`              | `[1, 2, 4, 6, 8, 9]` |
| `valid_group([5, 3, 4, 6, 7, 8, 9, 1, 2])`          | `True`      |
| `valid_group([5, 3, 4, 6, 7, 8, 9, 1, 1])`          | `False`     |
| `has_conflict([5, 3, 0, 0, 7, 0, 0, 0, 5])`         | `True`      |
| `has_conflict([5, 3, 0, 0, 7, 0, 0, 0, 0])`         | `False`     |

Hint: `set(range(1, 10))` is all nine digits. For conflicts, first make a list
without the zeros, then compare its length with the length of its set.
