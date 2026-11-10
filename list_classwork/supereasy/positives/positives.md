# Positive Numbers (Super Easy)

Keep only the numbers you need.

## Task

- Create a function `positives(nums)` that returns a new list with only the
  numbers **greater than 0**, in the same order
- Create a function `has_negative(nums)` that returns `True` if the list has
  at least one number less than 0

## Examples

| Call                          | Returns     |
|-------------------------------|-------------|
| `positives([3, -1, 0, 5])`    | `[3, 5]`    |
| `positives([-2, -7])`         | `[]`        |
| `has_negative([1, -1])`       | `True`      |
| `has_negative([0, 4])`        | `False`     |

Hint: `if n > 0:` then `append`.
