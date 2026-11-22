# Price List (Super Easy)

A shop keeps its prices in a dictionary: item name → price in somoni.

```python
prices = {"bread": 4, "milk": 9, "tea": 15, "sugar": 12}
```

## Task

- Create a function `total(prices, basket)` that returns how much the items in
  the list `basket` cost. An item can appear several times; an item the shop
  does not sell costs `0`
- Create a function `cheapest(prices)` that returns the name of the cheapest
  item. If several items share the lowest price, return the one that comes
  first alphabetically. An empty price list gives `None`

## Examples

| Call                                            | Returns    |
|-------------------------------------------------|------------|
| `total(prices, ["bread", "milk", "bread"])`     | `17`       |
| `total(prices, ["bread", "cake"])`              | `4`        |
| `total(prices, [])`                             | `0`        |
| `cheapest(prices)`                              | `"bread"`  |
| `cheapest({})`                                  | `None`     |

Hint: `prices.get(item, 0)`. For `cheapest`, loop over `sorted(prices)` and
keep the best name seen so far.
