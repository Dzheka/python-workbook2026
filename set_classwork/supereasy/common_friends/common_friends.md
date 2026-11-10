# Common Friends (Super Easy)

Ali and Sara each have a list of friends. Who do they both know?

## Task

- Create a function `common(a, b)` that returns the names that are in **both**
  lists, sorted alphabetically
- Create a function `only_first(a, b)` that returns the names that are in `a`
  but **not** in `b`, sorted alphabetically

A name can appear more than once in a list; the answer lists it once.

## Examples

| Call                                                   | Returns            |
|--------------------------------------------------------|--------------------|
| `common(["Bek", "Nilu", "Timur"], ["Nilu", "Bek"])`    | `["Bek", "Nilu"]`  |
| `common(["Bek"], ["Timur"])`                           | `[]`               |
| `only_first(["Bek", "Nilu", "Timur"], ["Nilu"])`       | `["Bek", "Timur"]` |

Hint: `&` and `-` on two sets, then `sorted(...)` gives a list.
