# Hexadecimal to Decimal

Write a function that converts a hexadecimal string to decimal.

## Task
- Create a function `hex_decimal(hex_str)` that takes a hexadecimal string
- Return the decimal (base 10) equivalent

## Examples

| Call                 | Returns |
|----------------------|---------|
| `hex_decimal("A")`   | `10`    |
| `hex_decimal("FF")`  | `255`   |
| `hex_decimal("10")`  | `16`    |
| `hex_decimal("1A")`  | `26`    |
| `hex_decimal("ABC")` | `2748`  |

## Note
- Don't use the built-in `int(hex_str, 16)`
- Accept both uppercase and lowercase letters
