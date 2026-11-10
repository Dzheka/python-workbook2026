# Game of Life (Hard)

Conway's Game of Life is played on an endless grid of cells. Each cell is
either alive or dead. We store only the **live** cells, as a set of
`(row, col)` tuples:

```python
blinker = {(1, 0), (1, 1), (1, 2)}     # three in a row
```

Every cell has 8 neighbours (up, down, left, right and the four diagonals).
Each step, all cells change at the same time:

- a live cell with **2 or 3** live neighbours stays alive
- a dead cell with **exactly 3** live neighbours comes alive
- every other cell is dead in the next step

## Task

- Create a function `neighbours(cell)` that returns the set of the 8 cells
  around `cell`
- Create a function `next_generation(live)` that returns the set of live cells
  after one step
- Create a function `run(live, steps)` that returns the live cells after
  `steps` steps (`0` steps gives the same cells back)

Rows and columns can become negative — the grid has no edges. Do not change
the set you are given.

## Examples

| Call                                          | Returns                              |
|-----------------------------------------------|--------------------------------------|
| `neighbours((0, 0))`                          | `{(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)}` |
| `next_generation({(1, 0), (1, 1), (1, 2)})`   | `{(0, 1), (1, 1), (2, 1)}`           |
| `run({(1, 0), (1, 1), (1, 2)}, 2)`            | `{(1, 0), (1, 1), (1, 2)}`           |
| `next_generation({(0, 0)})`                   | `set()`                              |

Hint: only live cells and their neighbours can be alive next step, so collect
those into a set of *candidates* with `|=`. For each candidate, the number of
live neighbours is `len(neighbours(cell) & live)`.
