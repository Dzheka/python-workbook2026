# Merge Sorted Lists (Medium)

Two lists are already sorted from smallest to largest. Combine them **without**
calling `sort`, `sorted`, `set` or `min`/`max`: walk both lists at once with
two indexes.

## Task

- Create a function `merge(a, b)` that returns one sorted list with all
  numbers from both lists (repeats stay)
- Create a function `common(a, b)` that returns a sorted list of the numbers
  found in **both** lists, each only once
- Create a function `only_in_first(a, b)` that returns a sorted list of the
  numbers in `a` that are not in `b`, each only once

## Examples

| Call                                     | Returns                  |
|------------------------------------------|--------------------------|
| `merge([1, 4, 9], [2, 3, 10])`           | `[1, 2, 3, 4, 9, 10]`    |
| `merge([], [5, 6])`                      | `[5, 6]`                 |
| `merge([1, 2], [2, 2])`                  | `[1, 2, 2, 2]`           |
| `common([1, 2, 2, 5, 7], [2, 2, 3, 7])`  | `[2, 7]`                 |
| `only_in_first([1, 2, 2, 5], [2, 3])`    | `[1, 5]`                 |

Hint: start with `i = j = 0`. Compare `a[i]` with `b[j]`, take the smaller
one and move only that index forward. When one list runs out, the rest of the
other one goes to the end.
