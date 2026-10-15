# Copy List

Create a copy of a list using slicing and prove it's a different object.

## Task

- Create a function `copy_list(l)` that takes a list
- Return a copy of the list (not the same object)
- Create a function `are_different_objects(l1, l2)` that checks if two lists are different objects

## Template:

```python
def copy_list(l: list) -> list:
    pass


def are_different_objects(l1: list, l2: list) -> bool:
    pass


if __name__ == "__main__":
    # Test your functions
    original = [2, 3, 5, 7, 11]
    copied = copy_list(original)
    print(copied)  # [2, 3, 5, 7, 11]
    print(are_different_objects(original, copied))  # True
```
