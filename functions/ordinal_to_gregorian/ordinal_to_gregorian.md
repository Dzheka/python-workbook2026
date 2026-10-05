# Ordinal to Gregorian Date

Write a function that converts an ordinal date (year + day of year) to Gregorian date (year, month, day).

## Task
- Create a function `ordinal_to_gregorian(year, day_of_year)` 
- Return a tuple (year, month, day)

## Examples

| Call                              | Returns          |
|-----------------------------------|------------------|
| `ordinal_to_gregorian(2024, 1)`   | `(2024, 1, 1)`   |
| `ordinal_to_gregorian(2024, 32)`  | `(2024, 2, 1)`   |
| `ordinal_to_gregorian(2024, 60)`  | `(2024, 2, 29)`  |
| `ordinal_to_gregorian(2023, 60)`  | `(2023, 3, 1)`   |
| `ordinal_to_gregorian(2024, 366)` | `(2024, 12, 31)` |
