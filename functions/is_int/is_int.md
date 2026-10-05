# Is Integer

Write a function that determines if a string represents a valid integer.

## Task
- Create a function `is_int(s)` that takes a string
- Return `True` if the string represents a valid integer, `False` otherwise

## Examples

| Call             | Returns |
|------------------|---------|
| `is_int("123")`  | `True`  |
| `is_int("-456")` | `True`  |
| `is_int("0")`    | `True`  |
| `is_int("12.5")` | `False` |
| `is_int("abc")`  | `False` |
| `is_int("")`     | `False` |
| `is_int("+789")` | `True`  |
| `is_int("12a")`  | `False` |

## Note
- A valid integer is an optional `+`/`-` sign followed by one or more digits
- An empty string, a lone sign, or surrounding whitespace is invalid
- Don't use built-in conversion functions like `int()`
