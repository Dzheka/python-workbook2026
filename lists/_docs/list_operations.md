# Lists in Python - Operations and Methods

## List Operations

### Length

```python
fruits = ["apple", "banana", "cherry"]
print(len(fruits))  # 3

empty = []
print(len(empty))  # 0
```

### Concatenation

```python
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Original lists unchanged
print(list1)  # [1, 2, 3]
```

### Repetition

```python
zeros = [0] * 5  # [0, 0, 0, 0, 0]
pattern = [1, 2] * 3  # [1, 2, 1, 2, 1, 2]
```

> **Note: Avoid using list multiplication!**
>
> While `[0] * 5` might seem convenient, **it's best to avoid list multiplication entirely** as it can lead to subtle
> bugs,
> especially with nested lists or when the code is modified later.
>
> **The problem**:
> ```python
> # DANGEROUS - creates references to the SAME inner list!
> matrix = [[0] * 3] * 3  # All rows point to the same list
> matrix[0][0] = 1
> print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - all rows modified!
> ```
>
> **Instead, always use list comprehensions or loops**:
> ```python
> # GOOD - clear and explicit
> zeros = [0 for _ in range(5)]
> matrix = [[0 for _ in range(3)] for _ in range(3)]
> ```
>
> List comprehensions are more explicit, easier to understand, and prevent the subtle reference bugs that multiplication
> can cause. They also make your code more maintainable when requirements change.

### Membership Testing

```python
fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)  # True
print("grape" in fruits)  # False
print("grape" not in fruits)  # True
```

### Comparison

```python
# Lexicographic comparison
print([1, 2, 3] == [1, 2, 3])  # True
print([1, 2] < [1, 2, 3])  # True (shorter, same prefix)
print([1, 3] > [1, 2, 5])  # True (3 > 2 at index 1)
```

## Common List Methods

Lists are **mutable** (can be changed after creation).

> **Note: What does "mutable" mean?**
>
> Mutable means the list can be modified after creation—you can add, remove, or change elements without creating a new
> list. This is different from immutable types like strings or tuples, which cannot be changed once created.
>
> **Important**: When you modify a list, all variables pointing to that list see the change. This is why understanding
> list copying (covered later) is crucial to avoid unexpected bugs.

| Method         | Description                 | Example                 | Result                        |
|----------------|-----------------------------|-------------------------|-------------------------------|
| `append(x)`    | Add x to end                | `[1, 2].append(3)`      | `[1, 2, 3]`                   |
| `insert(i, x)` | Insert x at index i         | `[1, 3].insert(1, 2)`   | `[1, 2, 3]`                   |
| `extend(iter)` | Add all items from iterable | `[1, 2].extend([3, 4])` | `[1, 2, 3, 4]`                |
| `remove(x)`    | Remove first x              | `[1, 2, 1].remove(1)`   | `[2, 1]`                      |
| `pop(i)`       | Remove and return item at i | `[1, 2, 3].pop(1)`      | Returns `2`, list is `[1, 3]` |
| `index(x)`     | Index of first x            | `[1, 2, 3].index(2)`    | `1`                           |
| `count(x)`     | Count occurrences of x      | `[1, 2, 1].count(1)`    | `2`                           |
| `sort()`       | Sort in place               | `[3, 1, 2].sort()`      | `[1, 2, 3]`                   |
| `reverse()`    | Reverse in place            | `[1, 2, 3].reverse()`   | `[3, 2, 1]`                   |
| `copy()`       | Shallow copy                | `[1, 2].copy()`         | `[1, 2]`                      |
| `clear()`      | Remove all items            | `[1, 2].clear()`        | `[]`                          |

> **Note: Methods that modify in-place vs return new values**
>
> Some methods modify the list directly (in-place) and return `None`:
> - `append()`, `extend()`, `insert()`, `remove()`, `pop()`, `sort()`, `reverse()`, `clear()`
>
> Others return a new value without modifying the original:
> - `sorted(list)` returns a new sorted list (vs `list.sort()` which sorts in-place)
> - `list[:]` creates a copy (vs assignment which creates a reference)
> - `reversed(list)` returns an iterator (vs `list.reverse()` which reverses in-place)
>
> **Common mistake**: Writing `numbers = numbers.sort()` will set `numbers` to `None` because `sort()` returns `None`!
