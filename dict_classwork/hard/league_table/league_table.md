# League Table (Hard)

Football matches are written as tuples `(home, home_goals, away_goals, away)`:

```python
matches = [
    ("Istiklol", 2, 1, "Khujand"),
    ("Ravshan", 0, 0, "Istiklol"),
    ("Khujand", 3, 0, "Ravshan"),
    ("Istiklol", 1, 2, "Ravshan"),
]
```

A win gives **3** points, a draw **1**, a loss **0**. Goal difference is goals
scored minus goals conceded.

## Task

- Create a function `standings(matches)` that returns the league table: a list
  of tuples `(team, played, points, goal_difference)`. Order: more points
  first; equal points → bigger goal difference first; still equal →
  alphabetically by name
- Create a function `leader(matches)` that returns the name of the team at the
  top of the table, or `None` if there are no matches

## Examples

`standings(matches)` returns

```python
[
    ("Istiklol", 3, 4, 0),
    ("Ravshan", 3, 4, -2),
    ("Khujand", 2, 3, 2),
]
```

and `leader(matches)` returns `"Istiklol"`.

Istiklol and Ravshan both have 4 points; Istiklol is higher thanks to a
better goal difference.

Hint: keep a dictionary `team → {"played": ..., "points": ..., "diff": ...}`
and update **both** teams after each match. Then turn it into tuples and sort
with `key=lambda row: (-row[2], -row[3], row[0])`.
