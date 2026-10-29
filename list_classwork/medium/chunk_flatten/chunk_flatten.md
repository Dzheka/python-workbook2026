# Chunks and Flatten (Medium)

Cut a list into pieces, glue pieces back together, and zip two lists into one.

## Task

- Create a function `chunk(items, size)` that cuts the list into pieces of
  `size` items; the last piece may be shorter
- Create a function `flatten(nested)` that glues a list of lists into one
  list (only one level deep)
- Create a function `interleave(a, b)` that takes items from `a` and `b` in
  turn: `a[0], b[0], a[1], b[1], ...`; when one list runs out, the rest of
  the other one is added at the end

`size` is always at least `1`.

## Examples

| Call                                     | Returns                           |
|------------------------------------------|-----------------------------------|
| `chunk([1, 2, 3, 4, 5], 2)`              | `[[1, 2], [3, 4], [5]]`           |
| `chunk([1, 2, 3], 5)`                    | `[[1, 2, 3]]`                     |
| `chunk([], 2)`                           | `[]`                              |
| `flatten([[1, 2], [], [3]])`             | `[1, 2, 3]`                       |
| `interleave([1, 2, 3], ["a", "b"])`      | `[1, "a", 2, "b", 3]`             |
| `interleave([], [7, 8])`                 | `[7, 8]`                          |

Hint: `range(0, len(items), size)` gives the start index of every piece.
`flatten(chunk(items, size))` should always give `items` back.
