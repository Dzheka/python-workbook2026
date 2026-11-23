# Flight Routes (Hard)

An airline flies between cities. Each flight is a pair `[from, to]` and goes
**one way only**.

```python
flights = [
    ["Dushanbe", "Moscow"], ["Dushanbe", "Istanbul"],
    ["Moscow", "Berlin"], ["Istanbul", "Berlin"],
    ["Berlin", "London"], ["London", "Dushanbe"],
    ["Khujand", "Moscow"],
]
```

## Task

- Create a function `direct(flights, city)` that returns the cities you can
  reach from `city` with **one** flight, sorted
- Create a function `reachable(flights, start)` that returns every city you
  can reach from `start` with any number of flights, sorted, **without**
  `start` itself
- Create a function `fewest_flights(flights, start, end)` that returns the
  smallest number of flights from `start` to `end` (`0` if they are the same
  city, `-1` if `end` cannot be reached)

## Examples

| Call                                                | Returns                                     |
|-----------------------------------------------------|---------------------------------------------|
| `direct(flights, "Dushanbe")`                       | `["Istanbul", "Moscow"]`                    |
| `reachable(flights, "Khujand")`                     | `["Berlin", "Dushanbe", "Istanbul", "London", "Moscow"]` |
| `fewest_flights(flights, "Dushanbe", "London")`     | `3`                                         |
| `fewest_flights(flights, "Berlin", "Khujand")`      | `-1`                                        |

Hint: first turn the list into a dictionary `city → set of next cities` with
`setdefault`. For the other two, keep a list of cities still to visit and a
dictionary `city → number of flights to get there`. Take cities from the
front of the list; a city already in the dictionary is not added again — that
is what stops you from flying in circles.
