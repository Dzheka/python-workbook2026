# Count Unique (Super Easy)

How many **different** things are in a list?

## Task

- Create a function `count_unique(items)` that returns how many different
  items the list has
- Create a function `all_different(items)` that returns `True` if no item
  appears twice

## Examples

| Call                                | Returns  |
|-------------------------------------|----------|
| `count_unique([3, 1, 3, 2, 1])`     | `3`      |
| `count_unique([])`                  | `0`      |
| `all_different(["a", "b", "c"])`    | `True`   |
| `all_different(["a", "b", "a"])`    | `False`  |

Hint: `set(items)` drops the duplicates. Compare its `len` with the list's.
