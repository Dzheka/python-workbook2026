# Lists in Python - Basics

## Introduction

Lists are ordered collections that can store multiple values in a single variable. They are one of the most versatile
and commonly used data structures in Python.

**Why use lists?**

| Benefit              | Description                                                |
|----------------------|------------------------------------------------------------|
| Group related values | Store multiple related values in a single variable         |
| Maintain order       | Elements keep their position and can be accessed by index  |
| Dynamic sizing       | Automatically grow or shrink as elements are added/removed |
| Efficient access     | Access any element by index in constant time               |
| Versatile storage    | Can store any data type (though typically homogeneous)     |

```python
# Instead of this:
score1 = 85
score2 = 92
score3 = 78

# Use this:
scores = [85, 92, 78]
```

## Creating Lists

| Method                | Example                                | Result                |
|-----------------------|----------------------------------------|-----------------------|
| Empty list (literal)  | `empty = []`                           | `[]`                  |
| Empty list (function) | `empty = list()`                       | `[]`                  |
| With values           | `numbers = [1, 2, 3, 4, 5]`            | `[1, 2, 3, 4, 5]`     |
| From range            | `list(range(5))`                       | `[0, 1, 2, 3, 4]`     |
| From range (step)     | `list(range(0, 11, 2))`                | `[0, 2, 4, 6, 8, 10]` |
| List comprehension    | `[x ** 2 for x in range(5)]`           | `[0, 1, 4, 9, 16]`    |
| With condition        | `[x for x in range(10) if x % 2 == 0]` | `[0, 2, 4, 6, 8]`     |
| Nested (2D)           | `[[1, 2], [3, 4]]`                     | `[[1, 2], [3, 4]]`    |
| Repeat elements       | `[0] * 5`                              | `[0, 0, 0, 0, 0]`     |
| From string           | `list("abc")`                          | `['a', 'b', 'c']`     |
| Split string          | `"1 2 3".split()`                      | `['1', '2', '3']`     |

### Examples

```python
# Numbers
numbers = [1, 2, 3, 4, 5]
prices = [19.99, 24.50, 15.75]

# Strings
names = ["Alice", "Bob", "Charlie"]
colors = ['red', 'green', 'blue']

# Nested lists (2D lists)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## Accessing Elements

### Indexing

Lists are zero-indexed (first element is at index 0):

```python
fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])  # "apple"  (first element)
print(fruits[1])  # "banana" (second element)
print(fruits[3])  # "date"   (fourth element)
# print(fruits[4]) # IndexError: list index out of range

# Negative Indexing - access elements from the end using negative indices
print(fruits[-1])  # "date"   (last element)
print(fruits[-2])  # "cherry" (second from end)
print(fruits[-4])  # "apple"  (fourth from end, same as fruits[0])
```

> **Note: Why does indexing start at 0?**
>
> Zero-based indexing comes from how computers store lists in memory. The index represents the **offset** (distance)
> from
> the start of the list:
>
> - Index `0` means "0 steps from the start" → first element
> - Index `1` means "1 step from the start" → second element
> - Index `n` means "n steps from the start" → (n+1)th element
>
> This makes array address calculations simpler and more efficient at the hardware level. Many programming languages (C,
> Java, JavaScript, Python) use zero-based indexing for this reason. While it may seem confusing at first, you'll
> quickly
> get used to thinking: "the first element is at index 0."

### Slicing

Extract sublists using `[start:stop:step]`:

| Syntax             | Example            | Result      |
|--------------------|--------------------|-------------|
| `list[start:stop]` | `[1,2,3,4,5][1:4]` | `[2, 3, 4]` |
| `list[start:]`     | `[1,2,3,4,5][2:]`  | `[3, 4, 5]` |
| `list[:stop]`      | `[1,2,3,4,5][:3]`  | `[1, 2, 3]` |
| `list[:]`          | `[1,2,3][:]`       | `[1, 2, 3]` |
| `list[::step]`     | `[1,2,3,4,5][::2]` | `[1, 3, 5]` |
| `list[::-1]`       | `[1,2,3][::-1]`    | `[3, 2, 1]` |
