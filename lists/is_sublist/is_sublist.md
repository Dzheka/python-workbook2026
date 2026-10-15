# Is Sublist

Check if one list is a sublist of another.

## Task

Write a function `is_sublist(main_list, sub)` that returns `True` if `sub` appears as consecutive elements in `main_list`, `False` otherwise.

- Elements must be consecutive: `[3, 7]` is not a sublist of `[2, 3, 5, 7, 11]`
- An empty list is a sublist of any list

## Template

```python
def is_sublist(main_list: list, sub: list) -> bool:
    pass


if __name__ == "__main__":
    print(is_sublist([2, 3, 5, 7, 11], [3, 5, 7]))  # True
    print(is_sublist([2, 3, 5, 7, 11], [3, 7]))  # False
    print(is_sublist([2, 3, 5], []))  # True
```
