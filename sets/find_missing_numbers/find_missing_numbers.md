# Find Missing Numbers

Find which numbers are missing from a range.

## Task

Write a function `find_missing(numbers, n)` that takes a list of numbers and an upper bound `n`, and returns a list of
all numbers from 1 to `n` (inclusive) that are **not** in the input list.

- The result should be sorted in ascending order
- Duplicates in the input list should be ignored

## Template

```python
def find_missing(numbers: list, n: int) -> list:
    pass


if __name__ == "__main__":
    print(find_missing([1, 2, 4, 6], 6))  # [3, 5]
    print(find_missing([2, 3, 7, 8], 10))  # [1, 4, 5, 6, 9, 10]
    print(find_missing([1, 2, 3], 3))  # []
    print(find_missing([], 5))  # [1, 2, 3, 4, 5]
    print(find_missing([1, 1, 2, 2], 4))  # [3, 4]
```
