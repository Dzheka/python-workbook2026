# Armstrong Numbers (Medium)

A number is an **Armstrong number** if it equals the sum of its digits, each
raised to the power of how many digits the number has:

```
153  = 1³ + 5³ + 3³ = 1 + 125 + 27
9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴
```

Every one-digit number is an Armstrong number.

## Task

- Create a function `count_digits(n)` that returns how many digits `n` has
  (`0` has one digit)
- Create a function `is_armstrong(n)` that returns `True` if `n` is an
  Armstrong number
- Create a function `count_armstrong(start, end)` that returns how many
  Armstrong numbers there are from `start` to `end`, both included
- Create a function `next_armstrong(n)` that returns the smallest Armstrong
  number greater than `n`

## Examples

| Call                          | Returns |
|-------------------------------|---------|
| `count_digits(153)`           | `3`     |
| `is_armstrong(153)`           | `True`  |
| `is_armstrong(154)`           | `False` |
| `count_armstrong(1, 1000)`    | `13`    |
| `count_armstrong(10, 99)`     | `0`     |
| `next_armstrong(9)`           | `153`   |
| `next_armstrong(407)`         | `1634`  |

Hint: count the digits first, then go over them a second time.
