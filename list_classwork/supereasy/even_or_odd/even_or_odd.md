# Even or Odd (Super Easy)

Look at every number in a list and say whether it is even or odd.

## Task

- Create a function `even_or_odd(nums)` that returns a new list with the word
  `"even"` or `"odd"` for every number
- Create a function `count_even(nums)` that returns how many numbers are even

## Examples

| Call                         | Returns                      |
|------------------------------|------------------------------|
| `even_or_odd([1, 2, 3])`     | `["odd", "even", "odd"]`     |
| `even_or_odd([])`            | `[]`                         |
| `count_even([2, 4, 5])`      | `2`                          |
| `count_even([1, 3])`         | `0`                          |

Hint: a number is even when `n % 2 == 0`.
