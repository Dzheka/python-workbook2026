# Club Members (Medium)

A school has a chess club and a football club. You get the list of all
students and the lists of each club's members.

## Task

- Create a function `in_both(chess, football)` — students in **both** clubs
- Create a function `in_exactly_one(chess, football)` — students in **one**
  club but not both
- Create a function `in_neither(students, chess, football)` — students in
  **no** club

Every function returns names sorted alphabetically, each name once.

## Examples

```python
students = ["Ali", "Bek", "Madina", "Nilu", "Sara", "Timur"]
chess = ["Ali", "Nilu", "Sara"]
football = ["Bek", "Sara", "Ali"]
```

| Call                                      | Returns                  |
|-------------------------------------------|--------------------------|
| `in_both(chess, football)`                | `["Ali", "Sara"]`        |
| `in_exactly_one(chess, football)`         | `["Bek", "Nilu"]`        |
| `in_neither(students, chess, football)`   | `["Madina", "Timur"]`    |

Hint: each function is one set operator (or two) and a `sorted`. Draw the two
circles if you are not sure which one.
