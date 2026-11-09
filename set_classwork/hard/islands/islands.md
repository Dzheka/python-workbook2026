# Islands (Hard)

A map is a list of strings: `#` is land and `.` is water.

```python
grid = [
    "##...",
    "#..#.",
    "...##",
    "#....",
]
```

Land cells that touch **up, down, left or right** belong to the same island
(touching only at a corner does not count). The map above has 3 islands: one
of size 3 in the top-left, one of size 3 on the right, and one of size 1 at
the bottom.

## Task

- Create a function `count_islands(grid)` that returns the number of islands
- Create a function `largest_island(grid)` that returns the number of cells in
  the biggest island, or `0` if there is no land

## Examples

| Call                                | Returns |
|-------------------------------------|---------|
| `count_islands(grid)`               | `3`     |
| `largest_island(grid)`              | `3`     |
| `count_islands(["#.#", ".#."])`     | `3`     |
| `largest_island(["...", "..."])`    | `0`     |

Hint: describe each cell by a tuple `(row, col)`. Collect all land cells in a
set. Keep a `seen` set: for every land cell not seen yet, you have found a new
island — explore it with a list used as a stack: pop a cell, push each of its
four neighbours that is land and not seen yet (add it to `seen` straight
away). The number of cells you popped is the island's size.
