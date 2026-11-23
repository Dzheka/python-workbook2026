# Inventory (Medium)

A warehouse keeps its stock in a dictionary: item → how many are left.

```python
stock = {"apples": 10, "pears": 4, "plums": 7}
```

## Task

- Create a function `restock(stock, delivery)` that returns a **new** stock
  after a delivery arrives. `delivery` is a dictionary of the same shape; new
  items are added, known items are increased
- Create a function `sell(stock, order)` that returns a **new** stock after an
  order is sent out. Items that drop to `0` disappear from the stock. If even
  **one** item in the order is missing or there is not enough of it, the whole
  order is refused: return `None`

Neither function changes the dictionaries it gets.

## Examples

| Call                                        | Returns                                     |
|---------------------------------------------|---------------------------------------------|
| `restock(stock, {"pears": 6, "kiwi": 3})`   | `{"apples": 10, "pears": 10, "plums": 7, "kiwi": 3}` |
| `sell(stock, {"apples": 3, "pears": 4})`    | `{"apples": 7, "plums": 7}`                 |
| `sell(stock, {"apples": 3, "pears": 5})`    | `None`                                      |
| `sell(stock, {"kiwi": 1})`                  | `None`                                      |

Hint: `dict(stock)` makes a copy. Check the whole order **before** you take
anything out.
