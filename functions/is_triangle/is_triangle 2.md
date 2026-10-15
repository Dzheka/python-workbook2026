# Is Triangle

Write a function that determines if three sides can form a triangle.

## Task
- Create a function `is_triangle(a, b, c)` that takes three side lengths
- Return `True` if they can form a triangle, `False` otherwise

## Examples

| Call                    | Returns |
|-------------------------|---------|
| `is_triangle(3, 4, 5)`  | `True`  |
| `is_triangle(1, 2, 3)`  | `False` |
| `is_triangle(5, 5, 5)`  | `True`  |
| `is_triangle(1, 1, 10)` | `False` |
| `is_triangle(7, 10, 5)` | `True`  |

## Rule
Triangle Inequality Theorem: the sum of any two sides must be greater than the third side.
- a + b > c
- a + c > b
- b + c > a

All three conditions must be true.
