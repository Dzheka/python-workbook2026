# Minesweeper (Hard)

A minefield is a list of strings of the same length. `"*"` is a mine and `"."`
is an empty square:

```python
field = [
    "*..",
    "...",
    ".*.",
]
```

Each square has up to 8 neighbours: left, right, up, down and the four
diagonals. Squares on the edge have fewer.

## Task

- Create a function `count_mines(field, r, c)` that returns how many of the
  neighbours of square `(r, c)` are mines (the square itself is not counted)
- Create a function `annotate(field)` that returns a new list of strings where
  every empty square is replaced by its number of neighbouring mines; a square
  with `0` stays `"."`, mines stay `"*"`
- Create a function `safe_squares(field)` that returns how many empty squares
  have **no** mines around them

## Examples

| Call                                      | Returns                     |
|-------------------------------------------|-----------------------------|
| `count_mines(["*..", "...", ".*."], 1, 1)`| `2`                         |
| `count_mines(["*..", "...", ".*."], 0, 2)`| `0`                         |
| `annotate(["*..", "...", ".*."])`         | `["*1.", "221", "1*1"]`     |
| `annotate(["..."])`                       | `["..."]`                   |
| `safe_squares(["*..", "...", ".*."])`     | `1`                         |

Hint: loop `dr` and `dc` over `-1, 0, 1`, skip `dr == dc == 0`, and check
that `r + dr` and `c + dc` are inside the field before looking at the square.
