# Longest Consecutive Sequence

Find the length of the longest sequence of consecutive numbers.

## Task

Write a function `longest_consecutive(numbers)` that finds the length of the longest sequence of consecutive integers in
the list.

- The numbers don't need to be adjacent in the list
- The order of numbers in the list doesn't matter
- Return 0 for an empty list

## Template

```python
def longest_consecutive(numbers: list) -> int:
    pass


if __name__ == "__main__":
    print(longest_consecutive([100, 4, 200, 1, 3, 2]))  # 4 (sequence: 1,2,3,4)
    print(longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9 (sequence: 0-8)
    print(longest_consecutive([1, 2, 0, 1]))  # 3 (sequence: 0,1,2)
    print(longest_consecutive([]))  # 0
    print(longest_consecutive([5]))  # 1
    print(longest_consecutive([1, 3, 5, 7]))  # 1 (no consecutive numbers)
```
