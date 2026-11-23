# Report Card (Super Easy)

A teacher stores test results in a dictionary: student name → score.

```python
grades = {"Ali": 85, "Sara": 92, "Bek": 67, "Nilu": 92}
```

## Task

- Create a function `average(grades)` that returns the average score, rounded
  to 1 decimal place (an empty dictionary gives `0`)
- Create a function `best_student(grades)` that returns the name with the
  highest score; if several students share it, return the one that comes
  first alphabetically (an empty dictionary gives `None`)
- Create a function `passed(grades, limit)` that returns the names of the
  students whose score is **at least** `limit`, sorted alphabetically

## Examples

| Call                       | Returns                       |
|----------------------------|-------------------------------|
| `average(grades)`          | `84.0`                        |
| `best_student(grades)`     | `"Nilu"`                      |
| `passed(grades, 85)`       | `["Ali", "Nilu", "Sara"]`     |
| `passed(grades, 100)`      | `[]`                          |

Hint: `grades.values()` gives the scores, `grades.items()` gives
`(name, score)` pairs.
