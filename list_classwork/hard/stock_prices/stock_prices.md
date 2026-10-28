# Stock Prices (Hard)

A list holds the price of one share on each day: `prices[0]` is day 0,
`prices[1]` is day 1, and so on.

## Task

- Create a function `max_profit(prices)` that returns the largest profit from
  buying **once** and selling **once** on a later day; if no deal makes money,
  return `0`
- Create a function `best_days(prices)` that returns `[buy_day, sell_day]` for
  that best deal; if several deals give the same profit, the one with the
  earliest buy day, then the earliest sell day; if no deal makes money, return
  `[]`
- Create a function `trend(prices)` that returns a string with one character
  per day after the first: `"+"` if the price went up, `"-"` if it went down,
  `"="` if it stayed the same

## Examples

| Call                                   | Returns       |
|----------------------------------------|---------------|
| `max_profit([7, 1, 5, 3, 6, 4])`       | `5`           |
| `max_profit([7, 6, 4, 3])`             | `0`           |
| `best_days([7, 1, 5, 3, 6, 4])`        | `[1, 4]`      |
| `best_days([7, 6, 4, 3])`              | `[]`          |
| `trend([3, 5, 5, 2])`                  | `"+=-"`       |
| `trend([10])`                          | `""`          |

Hint: two nested loops over `buy` and `sell` (with `sell > buy`) are enough.
For a faster way, remember the cheapest price seen so far while walking the
list once.
