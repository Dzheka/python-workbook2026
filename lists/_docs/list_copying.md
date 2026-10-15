# Lists in Python - Copying

## List Copying

### Shallow Copy vs Reference

```python
# Reference (not a copy!)
list1 = [1, 2, 3]
list2 = list1  # list2 points to same list
list2.append(4)
print(list1)  # [1, 2, 3, 4] - modified!

# Shallow copy (creates new list)
list1 = [1, 2, 3]
list2 = list1.copy()  # or list1[:] or list(list1)
list2.append(4)
print(list1)  # [1, 2, 3] - unchanged
print(list2)  # [1, 2, 3, 4]
```

> **Note: Why is this so important?**
>
> This is one of the **most common sources of bugs** for beginners! When you write `list2 = list1`, you're not creating
> a copy—you're creating another name (reference) for the same list in memory. Think of it like two people sharing the
> same notebook: when one person writes in it, the other sees the changes.
>
> **Rule of thumb**: Use `list2 = list1.copy()` or `list2 = list1[:]` whenever you want an independent copy that can be
> modified without affecting the original.

### Copy Methods

| Method             | Syntax                 | Creates New List | Notes                             |
|--------------------|------------------------|------------------|-----------------------------------|
| Assignment (NO!)   | `list2 = list1`        | ❌ No             | Both variables point to same list |
| `.copy()` method   | `list2 = list1.copy()` | ✅ Yes            | Recommended for clarity           |
| Slice notation     | `list2 = list1[:]`     | ✅ Yes            | Common idiom                      |
| `list()` function  | `list2 = list(list1)`  | ✅ Yes            | Explicit conversion               |
| `copy` module      | `copy.copy(list1)`     | ✅ Yes            | For shallow copy                  |
| `copy` module deep | `copy.deepcopy(list1)` | ✅ Yes            | For nested lists (deep copy)      |

```python
original = [1, 2, 3]

# Three ways to copy (all equivalent for simple lists)
copy1 = original.copy()
copy2 = original[:]
copy3 = list(original)

# All are independent copies
copy1.append(4)
print(original)  # [1, 2, 3]
print(copy1)  # [1, 2, 3, 4]
```
