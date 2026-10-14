# Date Tools (Hard)

Write a set of functions for dates from 1 January 1900 to 31 December 2100.
1 January 1900 was a Monday. Each function should build on the ones before
it.

## Task

- Create a function `is_leap_year(year)` that returns `True` for a leap year
- Create a function `days_in_month(month, year)` that returns the number of
  days in the month
- Create a function `day_of_year(day, month, year)` that returns which day of
  the year the date is (1 January is day 1)
- Create a function `weekday(day, month, year)` that returns the name of the
  weekday: `"Monday"`, `"Tuesday"`, ... `"Sunday"`
- Create a function `days_between(day1, month1, year1, day2, month2, year2)`
  that returns how many days lie between two dates; the result is never
  negative

## Examples

| Call                                  | Returns      |
|---------------------------------------|--------------|
| `is_leap_year(2024)`                  | `True`       |
| `is_leap_year(1900)`                  | `False`      |
| `days_in_month(2, 2000)`              | `29`         |
| `days_in_month(4, 2026)`              | `30`         |
| `day_of_year(1, 3, 2023)`             | `60`         |
| `day_of_year(31, 12, 2024)`           | `366`        |
| `weekday(1, 1, 2000)`                 | `"Saturday"` |
| `weekday(12, 10, 2026)`               | `"Monday"`   |
| `weekday(31, 12, 2100)`               | `"Friday"`   |
| `days_between(1, 1, 2026, 12, 10, 2026)` | `284`     |
| `days_between(12, 10, 2026, 1, 1, 2026)` | `284`     |
| `days_between(9, 9, 1991, 12, 10, 2026)` | `12817`   |
