# Shopping Total (Super Easy)

The prices of things in your basket are in a list.

## Task

- Create a function `total(prices)` that returns the sum of all prices
- Create a function `can_afford(prices, money)` that returns `"yes"` if
  `money` is enough to pay for everything, otherwise `"no"`

## Examples

| Call                           | Returns  |
|--------------------------------|----------|
| `total([10, 20, 5])`           | `35`     |
| `total([])`                    | `0`      |
| `can_afford([10, 20, 5], 50)`  | `"yes"`  |
| `can_afford([10, 20, 5], 35)`  | `"yes"`  |
| `can_afford([10, 20, 5], 30)`  | `"no"`   |

Hint: `can_afford` can call `total`.
