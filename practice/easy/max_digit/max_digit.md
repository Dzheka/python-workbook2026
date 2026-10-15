# Largest and Smallest Digit (Easy)

## Task

- Create a function `max_digit(n)` that returns the largest digit of `n`
- Create a function `min_digit(n)` that returns the smallest digit of `n`
- Create a function `digit_range(n)` that returns the largest digit minus
  the smallest

`n` may be negative; the minus sign is not a digit.

## Examples

| Call                  | Returns |
|-----------------------|---------|
| `max_digit(1234)`     | `4`     |
| `max_digit(-472)`     | `7`     |
| `min_digit(90817)`    | `0`     |
| `min_digit(5)`        | `5`     |
| `digit_range(90817)`  | `9`     |
| `digit_range(111)`    | `0`     |

Hint: `n % 10` is the last digit and `n // 10` removes it. Start from the
last digit, not from 0 — otherwise `min_digit(987)` would be 0.
