# Set Operations

Python gives you each of these operations as a built-in operator or method. Build them yourself to see what those shortcuts actually do.

## Task

Write five functions:

- `uniques(values)` — the elements of the list `values`, as a set
- `union(set1, set2)` — the elements that appear in either set
- `intersection(set1, set2)` — the elements that appear in both sets
- `is_subset(subset, superset)` — `True` if every element of `subset` is in `superset`
- `symmetric_diff(set1, set2)` — the elements that appear in exactly one of the two sets

Rules — the tests read your functions' source code and fail if you break them:

- Build result sets only with empty `set()` and `.add()`; no set literals, set comprehensions, or `set(iterable)` inside your functions
- No set operators: `|`, `&`, `-`, `^`, `<=`, `<`, `>`, `>=`
- No shortcut methods: `.union()`, `.intersection()`, `.difference()`, `.symmetric_difference()`, `.issubset()`, `.issuperset()`, `.isdisjoint()`, `.update()`, and the other `*_update()` methods

## Template

```python
def uniques(values: list) -> set:
    pass


def union(set1: set, set2: set) -> set:
    pass


def intersection(set1: set, set2: set) -> set:
    pass


def is_subset(subset: set, superset: set) -> bool:
    pass


def symmetric_diff(set1: set, set2: set) -> set:
    pass


if __name__ == "__main__":
    print(uniques([2, 3, 3, 5, 5, 5]))  # {2, 3, 5}
    print(union({2, 3, 5}, {5, 7, 11}))  # {2, 3, 5, 7, 11}
    print(intersection({2, 3, 5, 7}, {5, 7, 11, 13}))  # {5, 7}
    print(is_subset({2, 3}, {2, 3, 5, 7}))  # True
    print(is_subset({2, 11}, {2, 3, 5, 7}))  # False
    print(symmetric_diff({2, 3, 5}, {3, 5, 7}))  # {2, 7}
```
