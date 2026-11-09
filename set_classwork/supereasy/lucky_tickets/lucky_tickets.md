# Lucky Tickets (Super Easy)

You bought some lottery tickets. Today's winning numbers were announced.

## Task

- Create a function `winning(tickets, winners)` that returns your ticket
  numbers that are also winners, each once, sorted from smallest to largest
- Create a function `has_winner(tickets, winners)` that returns `True` if at
  least one of your tickets wins

## Examples

| Call                                      | Returns   |
|-------------------------------------------|-----------|
| `winning([12, 7, 30, 7], [7, 30, 41])`    | `[7, 30]` |
| `winning([1, 2], [3])`                    | `[]`      |
| `has_winner([1, 2], [2, 5])`              | `True`    |
| `has_winner([1, 2], [])`                  | `False`   |

Hint: `&` for the first; for the second, two sets with nothing in common are
called *disjoint*.
