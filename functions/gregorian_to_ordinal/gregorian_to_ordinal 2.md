# Gregorian to Ordinal Date

Write a function that converts a Gregorian date to ordinal date (day of year).

## Task
- Create a function `gregorian_to_ordinal(year, month, day)` 
- Return the day of the year (1-366)

## Examples

| Call                                 | Returns |
|--------------------------------------|---------|
| `gregorian_to_ordinal(2024, 1, 1)`   | `1`     |
| `gregorian_to_ordinal(2024, 2, 1)`   | `32`    |
| `gregorian_to_ordinal(2024, 2, 29)`  | `60`    |
| `gregorian_to_ordinal(2023, 3, 1)`   | `60`    |
| `gregorian_to_ordinal(2024, 12, 31)` | `366`   |
