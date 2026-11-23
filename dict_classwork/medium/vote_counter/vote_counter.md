# Vote Counter (Medium)

A class votes for its new monitor. Every vote is one name in a list.

```python
votes = ["Sara", "Ali", "Sara", "Bek", "Ali", "Sara"]
```

## Task

- Create a function `tally(votes)` that returns a dictionary: candidate →
  number of votes
- Create a function `winner(votes)` that returns the candidate with the most
  votes. On a tie, the name that comes first alphabetically wins. No votes
  gives `None`
- Create a function `percentages(votes)` that returns a dictionary: candidate
  → their share of all votes in percent, rounded to 1 decimal place

## Examples

| Call                                | Returns                                   |
|-------------------------------------|-------------------------------------------|
| `tally(votes)`                      | `{"Sara": 3, "Ali": 2, "Bek": 1}`         |
| `winner(votes)`                     | `"Sara"`                                  |
| `winner(["Bek", "Ali"])`            | `"Ali"`                                   |
| `percentages(votes)`                | `{"Sara": 50.0, "Ali": 33.3, "Bek": 16.7}`|
| `percentages([])`                   | `{}`                                      |

Hint: build `tally` first and use it in the other two functions.
