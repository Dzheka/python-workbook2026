# Triangle Numbers (Medium)

Stack balls in a triangle — 1 in the first row, 2 in the second, and so on.
The total number of balls is a **triangle number**:

```
●        ●        ●          ●
        ● ●      ● ●        ● ●
                ● ● ●      ● ● ●
                          ● ● ● ●
1        3        6         10
```

The `n`-th triangle number is `1 + 2 + ... + n`.

## Task

- Create a function `nth_triangle(n)` that returns the `n`-th triangle number
  (`0` for `n = 0`)
- Create a function `triangle_index(x)` that returns `n` if `x` is the `n`-th
  triangle number, or `-1` if `x` is not a triangle number
- Create a function `is_triangular(x)` that returns `True` or `False`
- Create a function `count_triangular(start, end)` that returns how many
  triangle numbers there are from `start` to `end`, both included

## Examples

| Call                          | Returns |
|-------------------------------|---------|
| `nth_triangle(4)`             | `10`    |
| `nth_triangle(100)`           | `5050`  |
| `triangle_index(55)`          | `10`    |
| `triangle_index(54)`          | `-1`    |
| `is_triangular(28)`           | `True`  |
| `count_triangular(1, 10)`     | `4`     |
| `count_triangular(1, 100)`    | `13`    |

Hint for `triangle_index`: keep adding 1, 2, 3, ... until the total reaches
or passes `x`.
