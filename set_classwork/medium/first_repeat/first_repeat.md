# First Repeat (Medium)

Walk through a list and remember what you have already seen.

## Task

- Create a function `first_repeat(items)` that returns the first item that
  turns up for a **second** time while walking left to right, or `None` if
  nothing repeats
- Create a function `remove_repeats(items)` that returns a new list where
  every item appears once, in the order it **first** appeared

The original list must not change.

## Examples

| Call                                          | Returns              |
|-----------------------------------------------|----------------------|
| `first_repeat(["red", "blue", "green", "blue", "red"])` | `"blue"`   |
| `first_repeat([1, 2, 3])`                     | `None`               |
| `remove_repeats([3, 1, 3, 2, 1])`             | `[3, 1, 2]`          |
| `remove_repeats([])`                          | `[]`                 |

In the first example `"red"` appears first, but `"blue"` is the first to be
seen **again**.

Hint: a `seen = set()` beside the loop. `list(set(items))` does not keep the
order, so it will not pass the tests.
