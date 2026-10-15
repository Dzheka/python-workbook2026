# Taxi Fare (Easy)

A taxi company charges:

- a fixed **5.00** for getting in
- **2.00** per km for the first 10 km
- **1.50** per km for every km after the first 10
- at night the whole price is **25% higher**

## Task

- Create a function `fare(km, night)` that returns the price of a ride of
  `km` kilometres (`night` is `True` or `False`), rounded to 2 decimals

## Examples

| Call               | Returns |
|--------------------|---------|
| `fare(0, False)`   | `5.0`   |
| `fare(4, False)`   | `13.0`  |
| `fare(10, False)`  | `25.0`  |
| `fare(14, False)`  | `31.0`  |
| `fare(14, True)`   | `38.75` |
| `fare(2.5, True)`  | `12.5`  |

For 14 km: 5 + 10 · 2 + 4 · 1.5 = 31.
