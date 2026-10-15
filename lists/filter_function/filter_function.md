# Filter Function

Implement a custom filter function that filters a list based on a callable condition.

## Task

- Create a function `filter_list(l, condition)` that takes a list and a callable function
- Return a new list containing only elements that satisfy the condition
- The condition is a function that returns True or False

## Template:

```python
from typing import Callable


def filter_list(l: list, condition: Callable) -> list:
    pass


if __name__ == "__main__":
    # Test your function
    def is_even(x):
        return x % 2 == 0


    print(filter_list([11, 4, 7, 22, 9], is_even))  # [4, 22]


    def is_positive(x):
        return x > 0


    print(filter_list([-2, -1, 0, 1, 2], is_positive))  # [1, 2]
```
