# Roman Numerals (Hard)

Write three functions that convert between integers and Roman numerals.

| Symbol | I | V | X  | L  | C   | D   | M    |
|--------|---|---|----|----|-----|-----|------|
| Value  | 1 | 5 | 10 | 50 | 100 | 500 | 1000 |

A smaller symbol before a larger one is subtracted: `IV` = 4, `IX` = 9,
`XL` = 40, `XC` = 90, `CD` = 400, `CM` = 900.

## Task

- Create a function `to_roman(n)` that returns `n` (1 ≤ n ≤ 3999) as a Roman
  numeral
- Create a function `from_roman(text)` that returns the integer value of a
  valid Roman numeral
- Create a function `is_roman(text)` that returns `True` only if `text` is a
  Roman numeral written the standard way, with a value from 1 to 3999;
  use `to_roman` and `from_roman` inside it

## Examples

| Call                     | Returns       |
|--------------------------|---------------|
| `to_roman(14)`           | `"XIV"`       |
| `to_roman(1994)`         | `"MCMXCIV"`   |
| `to_roman(3999)`         | `"MMMCMXCIX"` |
| `from_roman("XIV")`      | `14`          |
| `from_roman("MCMXCIV")`  | `1994`        |
| `from_roman("MMXXVI")`   | `2026`        |
| `is_roman("MMXXVI")`     | `True`        |
| `is_roman("IIII")`       | `False`       |
| `is_roman("IC")`         | `False`       |
| `is_roman("MMMM")`       | `False`       |
| `is_roman("ABC")`        | `False`       |
| `is_roman("")`           | `False`       |
