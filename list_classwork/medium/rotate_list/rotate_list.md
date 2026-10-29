# Rotate a List (Medium)

Rotating a list moves its items around in a circle:

```
rotate left by 1:   [1, 2, 3, 4]  ->  [2, 3, 4, 1]
rotate right by 1:  [1, 2, 3, 4]  ->  [4, 1, 2, 3]
```

Rotating by the length of the list gives the same list back, so rotating
`[1, 2, 3, 4]` by `6` is the same as rotating it by `2`.

## Task

- Create a function `rotate_left(items, k)` that returns a **new** list
  rotated left by `k`
- Create a function `rotate_right(items, k)` that returns a **new** list
  rotated right by `k`
- Create a function `is_rotation(a, b)` that returns `True` if `b` is some
  rotation of `a` (a list is a rotation of itself)

`k` is never negative. An empty list stays empty. The original list must not
change.

## Examples

| Call                                   | Returns          |
|----------------------------------------|------------------|
| `rotate_left([1, 2, 3, 4], 1)`         | `[2, 3, 4, 1]`   |
| `rotate_left([1, 2, 3, 4], 6)`         | `[3, 4, 1, 2]`   |
| `rotate_right([1, 2, 3, 4], 1)`        | `[4, 1, 2, 3]`   |
| `rotate_right([], 3)`                  | `[]`             |
| `is_rotation([1, 2, 3], [3, 1, 2])`    | `True`           |
| `is_rotation([1, 2, 3], [1, 3, 2])`    | `False`          |

Hint: slices do the work: `items[k:] + items[:k]`. Use `k % len(items)` so
`k` is never larger than the list, and watch out for the empty list.
