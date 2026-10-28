# Change in Coins (Medium)

A cashier has coins of **50, 20, 10, 5, 2 and 1** and always pays change with
as few coins as possible: take the largest coin that still fits, as many
times as it fits, then move to the next one.

## Task

- Create a function `count_coins(amount)` that returns how many coins the
  cashier gives for `amount`
- Create a function `coin_breakdown(amount)` that returns which coins, from
  the largest: `"2x50 1x20 1x5"` — coins that are not used are left out, and
  `0` gives an empty string
- Create a function `can_pay(amount, max_coins)` that returns `True` if the
  change fits into `max_coins` coins

## Examples

| Call                       | Returns                          |
|----------------------------|----------------------------------|
| `count_coins(4)`           | `2`                              |
| `count_coins(88)`          | `6`                              |
| `coin_breakdown(125)`      | `"2x50 1x20 1x5"`                |
| `coin_breakdown(99)`       | `"1x50 2x20 1x5 2x2"`            |
| `coin_breakdown(0)`        | `""`                             |
| `can_pay(125, 4)`          | `True`                           |
| `can_pay(99, 5)`           | `False`                          |

Hint: loop over the coins with `for coin in (50, 20, 10, 5, 2, 1):` and use
`//` and `%`.
