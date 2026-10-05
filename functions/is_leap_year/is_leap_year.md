# Is Leap Year

Write a function that determines if a year is a leap year.

## Task
- Create a function `is_leap_year(year)` that takes a year
- Return `True` if it's a leap year, `False` otherwise

## Examples

| Call                 | Returns |
|----------------------|---------|
| `is_leap_year(2000)` | `True`  |
| `is_leap_year(2004)` | `True`  |
| `is_leap_year(1900)` | `False` |
| `is_leap_year(2001)` | `False` |
| `is_leap_year(2024)` | `True`  |

## Rule
A year is a leap year if:
- It's divisible by 4, AND
- If it's divisible by 100, it must also be divisible by 400
