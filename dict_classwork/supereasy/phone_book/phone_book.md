# Phone Book (Super Easy)

A phone book is a dictionary: the key is a name, the value is a phone number.

```python
book = {"Ali": "901-11-22", "Sara": "933-44-55", "Bek": "918-00-01"}
```

## Task

- Create a function `lookup(book, name)` that returns the number of `name`, or
  the string `"not found"` if there is no such contact
- Create a function `names(book)` that returns all names, sorted
  alphabetically
- Create a function `has_number(book, number)` that returns `True` if some
  contact has this number, otherwise `False`

## Examples

| Call                              | Returns                   |
|-----------------------------------|---------------------------|
| `lookup(book, "Sara")`            | `"933-44-55"`             |
| `lookup(book, "Timur")`           | `"not found"`             |
| `names(book)`                     | `["Ali", "Bek", "Sara"]`  |
| `has_number(book, "918-00-01")`   | `True`                    |
| `has_number(book, "000-00-00")`   | `False`                   |

Hint: `book.get(name, default)`, `sorted(book)` and `book.values()`.
