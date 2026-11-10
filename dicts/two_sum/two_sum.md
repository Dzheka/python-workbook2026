# Two Sum

Find two numbers that add up to a target value.

## Task

Write a function `two_sum(nums, target)` that finds two numbers in the list that add up to the target value.

- Return the indices of the two numbers as a list `[index1, index2]`
- Return `None` if no two numbers add up to the target
- You cannot use the same element twice
- There may be multiple valid answers; return any one of them

## Template

```python
def two_sum(nums: list[int], target: int) -> list[int] | None:
    pass


if __name__ == "__main__":
    print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
    print(two_sum([3, 2, 4], 6))  # [1, 2]
    print(two_sum([3, 3], 6))  # [0, 1]
    print(two_sum([2, 3, 5], 10))  # None
    print(two_sum([-1, -2, -3, -4], -5))  # [0, 3] or [1, 2]
    print(two_sum([0, 1, 0], 0))  # [0, 2]
```
