# Greet Everyone (Super Easy)

You have a list of names. Say hello to each one.

## Task

- Create a function `greet_all(names)` that returns a new list with
  `"Hello, <name>!"` for every name
- Create a function `count_long_names(names)` that returns how many names have
  **more than 4** letters

## Examples

| Call                                    | Returns                              |
|-----------------------------------------|--------------------------------------|
| `greet_all(["Ali", "Sara"])`            | `["Hello, Ali!", "Hello, Sara!"]`    |
| `greet_all([])`                         | `[]`                                 |
| `count_long_names(["Ali", "Firuz"])`    | `1`                                  |

Hint: start with an empty list `result = []` and use `result.append(...)`
inside a `for` loop.
