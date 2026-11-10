# Class Report (Hard)

Each student is a list of two items, a name and a score from `0` to `100`:

```python
records = [["Ali", 85], ["Sara", 92], ["Firuz", 85], ["Madina", 47]]
```

Letter grades: `A` for 90 and above, `B` for 80–89, `C` for 70–79, `D` for
60–69, `F` below 60.

## Task

- Create a function `letter(score)` that returns the letter grade
- Create a function `ranking(records)` that returns the names ordered from
  the highest score down; students with the same score are ordered by name
  alphabetically
- Create a function `report(records)` that returns one line per student, in
  ranking order, joined with `"\n"`:
  `"<place>. <name> - <score> (<letter>)"`. Students with the same score share
  the same place, and the next place skips accordingly (`1, 2, 2, 4`)
- Create a function `failed(records)` that returns the names of students with
  an `F`, in the original order

The original list must not change.

## Examples

```python
>>> print(report([["Ali", 85], ["Sara", 92], ["Firuz", 85], ["Madina", 47]]))
1. Sara - 92 (A)
2. Ali - 85 (B)
2. Firuz - 85 (B)
4. Madina - 47 (F)
```

| Call                                                | Returns                    |
|-----------------------------------------------------|----------------------------|
| `letter(79)`                                        | `"C"`                      |
| `ranking([["Bo", 70], ["Al", 70], ["Cy", 90]])`     | `["Cy", "Al", "Bo"]`       |
| `failed([["Ali", 59], ["Sara", 60], ["Bo", 10]])`   | `["Ali", "Bo"]`            |
| `report([])`                                        | `""`                       |

Hint: `sorted(records, key=lambda r: (-r[1], r[0]))` gives the ranking order.
For the places: a student's place is `1 +` the number of students with a
strictly higher score.
