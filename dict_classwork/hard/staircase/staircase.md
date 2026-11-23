# Staircase (Hard)

You climb a staircase of `n` steps. With one move you can go up by any number
from the list `steps` — for example `[1, 2]` means one or two steps at a time.

In how many different ways can you get exactly to the top? The order of moves
matters: `1 + 2` and `2 + 1` are two different ways.

## Task

- Create a function `ways(n, steps)` that returns the number of ways to reach
  step `n`. There is exactly **one** way to climb `0` steps: do nothing
- Create a function `min_steps(n, steps)` that returns the smallest number of
  moves that reaches step `n` exactly, or `-1` if it cannot be done

## Examples

| Call                       | Returns   |
|----------------------------|-----------|
| `ways(3, [1, 2])`          | `3`       |
| `ways(4, [1, 2])`          | `5`       |
| `ways(5, [2])`             | `0`       |
| `min_steps(7, [1, 3, 5])`  | `3`       |
| `min_steps(7, [2, 4])`     | `-1`      |

The three ways for `ways(3, [1, 2])` are `1+1+1`, `1+2` and `2+1`.

The tests also ask for `ways(200, [1, 2])`. The straightforward recursion
recomputes the same answers again and again and would run for years. Store
every answer you have already found in a dictionary (a **cache**, or *memo*)
and look it up before computing.

Hint: the ways to reach `n` = the sum, over every move `s` in `steps`, of the
ways to reach `n - s`. For `min_steps`, fill a dictionary `best` for
`0, 1, 2, ..., n` in order: `best[i]` is `1 + ` the smallest `best[i - s]`
that exists.
