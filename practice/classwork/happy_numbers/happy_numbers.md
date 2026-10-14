# Happy Numbers (Hard)

Take a positive number, replace it with the sum of the squares of its digits,
and repeat:

```
19 → 1² + 9² = 82 → 8² + 2² = 68 → 6² + 8² = 100 → 1² + 0² + 0² = 1
```

If the process reaches `1`, the number is **happy**. If it never does, it gets
stuck in a loop forever — and every such loop passes through `4`:

```
2 → 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...
```

So: repeat until you reach `1` (happy) or `4` (not happy).

## Task

- Create a function `square_digit_sum(n)` that returns the sum of the squares
  of the digits of `n`
- Create a function `is_happy(n)` that returns `True` if `n` is happy
- Create a function `count_happy(start, end)` that returns how many happy
  numbers there are from `start` to `end`, both included
- Create a function `nth_happy(k)` that returns the `k`-th happy number,
  counting from 1: the happy numbers are 1, 7, 10, 13, 19, 23, ...

Each function should use the one before it.

## Examples

| Call                     | Returns |
|--------------------------|---------|
| `square_digit_sum(19)`   | `82`    |
| `square_digit_sum(999)`  | `243`   |
| `is_happy(19)`           | `True`  |
| `is_happy(2)`            | `False` |
| `count_happy(1, 10)`     | `3`     |
| `count_happy(1, 100)`    | `20`    |
| `nth_happy(2)`           | `7`     |
| `nth_happy(5)`           | `19`    |

Hint: digits come out of a number with `% 10` and `// 10` — no strings needed.
