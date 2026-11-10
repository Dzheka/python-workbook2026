# Tic-Tac-Toe (Hard)

A tic-tac-toe board is a list of 3 strings, one per row. Each character is
`"X"`, `"O"` or `"."` for an empty square:

```python
board = [
    "XO.",
    "XO.",
    "X..",
]
```

A player wins with three of their marks in a row, a column or a diagonal.

## Task

- Create a function `lines(board)` that returns a list of all 8 lines as
  strings: the 3 rows, then the 3 columns (left to right), then the diagonal
  from the top-left and the diagonal from the top-right
- Create a function `winner(board)` that returns `"X"`, `"O"`, or `""` if
  nobody has won
- Create a function `game_state(board)` that returns `"X wins"`, `"O wins"`,
  `"draw"` (board full, no winner) or `"in progress"`

You may assume at most one player has won.

## Examples

| Call                                    | Returns                                               |
|-----------------------------------------|-------------------------------------------------------|
| `lines(["XO.", "XO.", "X.."])`          | `["XO.", "XO.", "X..", "XXX", "OO.", "...", "XO.", ".OX"]` |
| `winner(["XO.", "XO.", "X.."])`         | `"X"`                                                 |
| `winner(["...", "...", "..."])`         | `""`                                                  |
| `game_state(["XOX", "XOO", "OXX"])`     | `"draw"`                                              |
| `game_state(["OX.", "XO.", "..O"])`     | `"O wins"`                                            |
| `game_state(["X..", "...", "..."])`     | `"in progress"`                                       |

Hint: `board[r][c]` is the square in row `r`, column `c`. Once you have
`lines`, `winner` only needs to look for `"XXX"` or `"OOO"` among them.
