# Bingo (Hard)

A bingo card is a square grid of numbers (usually 5×5). The host calls out
numbers; every number on your card that has been called is *marked*. The
middle cell is often free: on these cards a free cell is written as `0` and
counts as marked from the start.

You win (*bingo!*) when a whole **row**, a whole **column**, or one of the two
**diagonals** is marked.

```python
card = [
    [ 5, 18, 33, 48, 64],
    [12, 21, 31, 52, 70],
    [ 3, 26,  0, 47, 61],
    [ 9, 17, 38, 55, 68],
    [14, 29, 41, 50, 75],
]
```

## Task

- Create a function `marked(card, called)` that returns how many cells of the
  card are marked (free cells included)
- Create a function `has_bingo(card, called)` that returns `True` if some
  row, column or diagonal is completely marked

`called` is a list of numbers and may contain numbers that are not on the
card. The card can be any size `n × n`.

## Examples

| Call                                                | Returns   |
|-----------------------------------------------------|-----------|
| `marked(card, [5, 99, 21])`                         | `3`       |
| `has_bingo(card, [3, 26, 47, 61])`                  | `True`    |
| `has_bingo(card, [5, 21, 55, 75])`                  | `True`    |
| `has_bingo(card, [5, 12, 3, 9])`                    | `False`   |

The second is the middle row (with the free `0`), the third is the diagonal,
the last misses `14` to finish the first column.

Hint: put `called` and `0` into one set first. Then build every line (rows,
columns, two diagonals) as a list and ask whether `set(line) <= called_set`.
