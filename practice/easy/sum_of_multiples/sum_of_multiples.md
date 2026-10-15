# Sum of Multiples (Easy)

The numbers below 10 that are divisible by 3 or by 5 are 3, 5, 6 and 9.
There are 4 of them, and their sum is 23.

## Task

- Create a function `count_multiples(limit, a, b)` that returns how many
  numbers from 1 up to `limit` (not included) are divisible by `a` or by `b`
- Create a function `sum_multiples(limit, a, b)` that returns their sum

A number divisible by both counts only once.

## Examples

| Call                          | Returns  |
|-------------------------------|----------|
| `count_multiples(10, 3, 5)`   | `4`      |
| `count_multiples(16, 3, 5)`   | `7`      |
| `sum_multiples(10, 3, 5)`     | `23`     |
| `sum_multiples(16, 3, 5)`     | `60`     |
| `sum_multiples(1000, 3, 5)`   | `233168` |
