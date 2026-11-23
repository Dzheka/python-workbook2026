# Sales Report (Hard)

A company sells in several regions. Every sale is a tuple
`(region, product, amount)`.

```python
sales = [
    ("Sughd", "tea", 120),
    ("Khatlon", "rice", 300),
    ("Sughd", "rice", 80),
    ("Sughd", "tea", 50),
    ("Khatlon", "tea", 40),
    ("GBAO", "honey", 90),
]
```

## Task

- Create a function `by_region(sales)` that returns a dictionary: region →
  total amount sold there
- Create a function `report(sales)` that returns a **nested** dictionary:
  region → (product → total amount of that product in that region)
- Create a function `best_sellers(sales)` that returns a dictionary: region →
  the product with the biggest total there. On a tie, the product that comes
  first alphabetically

## Examples

| Call                 | Returns                                                                 |
|----------------------|-------------------------------------------------------------------------|
| `by_region(sales)`   | `{"Sughd": 250, "Khatlon": 340, "GBAO": 90}`                            |
| `report(sales)`      | `{"Sughd": {"tea": 170, "rice": 80}, "Khatlon": {"rice": 300, "tea": 40}, "GBAO": {"honey": 90}}` |
| `best_sellers(sales)`| `{"Sughd": "tea", "Khatlon": "rice", "GBAO": "honey"}`                  |

Hint: in `report`, `products = nested.setdefault(region, {})` gives you the
inner dictionary of a region (creating it the first time). `best_sellers` is
easy once `report` works.
