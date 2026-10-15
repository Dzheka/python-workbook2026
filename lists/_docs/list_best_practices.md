# Lists in Python - Best Practices and Quick Reference

## Common Mistakes

### 1. Index Out of Range

```python
numbers = [1, 2, 3]
# print(numbers[3])  # IndexError!

# Safe access
if 3 < len(numbers):
    print(numbers[3])
```

### 2. Modifying List While Iterating

```python
# WRONG
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num % 2 == 0:
        numbers.remove(num)  # Don't modify while iterating!

# CORRECT - iterate over copy
numbers = [1, 2, 3, 4, 5]
for num in numbers[:]:
    if num % 2 == 0:
        numbers.remove(num)

# BETTER - use list comprehension
numbers = [1, 2, 3, 4, 5]
numbers = [num for num in numbers if num % 2 != 0]
```

> **Note: Why does modifying while iterating fail?**
>
> When you modify a list during iteration (adding/removing elements), you change the list's size and structure while
> Python is trying to iterate through it. This causes elements to be skipped or processed multiple times.
>
> **Example**: If you remove an element at index 2, what was at index 3 moves to index 2, but the loop has already moved
> to index 3, skipping the element that moved!
>
> **Solution**: Either iterate over a copy (`for item in list[:]`), or use list comprehension to create a filtered list.

### 3. Creating 2D Lists Incorrectly

```python
# WRONG - creates references to same list
matrix = [[0] * 3] * 3
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [1, 0, 0], [1, 0, 0]] - all rows modified!

# CORRECT
matrix = [[0] * 3 for _ in range(3)]
matrix[0][0] = 1
print(matrix)  # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
```

> **Note: Why does `[[0] * 3] * 3` create references?**
>
> When you use `[[0] * 3] * 3`, Python creates one inner list `[0, 0, 0]` and then creates three references to that
> **same** list. It's like making 3 variables all point to the same list!
>
> Think of it this way:
> - `[0] * 3` creates `[0, 0, 0]` (one list)
> - `[[0, 0, 0]] * 3` creates three references to that one list
>
> **Solution**: Use a list comprehension `[[0] * 3 for _ in range(3)]` which creates a new independent list in each
> iteration. The `for _ in range(3)` ensures you create 3 separate lists, not 3 references to the same list.

## Best Practices

| Practice                      | ✅ Good                               | ❌ Avoid                                 |
|-------------------------------|--------------------------------------|-----------------------------------------|
| **Transformations**           | `[x*2 for x in nums]`                | Manual loop with append                 |
| **Membership testing**        | `if item in my_list:`                | `for x in my_list: if x == item:`       |
| **Built-in functions**        | `sum(numbers)`, `max(numbers)`       | Manual loops for sum/max/min            |
| **Iteration with index**      | `for i, val in enumerate(list):`     | `for i in range(len(list)):`            |
| **Copying**                   | `new = old.copy()` or `new = old[:]` | `new = old` (creates reference!)        |
| **Naming**                    | `students`, `scores`, `temperatures` | `list1`, `data`, `arr`                  |
| **Type consistency**          | `numbers = [1, 2, 3]`                | `mixed = [1, "two", 3.0]`               |
| **Bounds checking**           | `if i < len(list): list[i]`          | Direct access without checking          |
| **Modifying while iterating** | `for item in my_list[:]:` (copy)     | `for item in my_list:` then modify      |
| **Creating 2D lists**         | `[[0]*cols for _ in range(rows)]`    | `[[0]*cols]*rows` (creates references!) |
| **Reversing**                 | `reversed_list = my_list[::-1]`      | Manual reverse with indices             |
| **Sorting**                   | `sorted(list)` or `list.sort()`      | Manual sorting algorithm                |

## Quick Reference

```python
# Creating
empty = []
numbers = [1, 2, 3]
from_range = list(range(10))

# Accessing
first = numbers[0]
last = numbers[-1]
slice = numbers[1:3]

# Modifying
numbers.append(4)  # Add to end
numbers.insert(0, 0)  # Insert at position
numbers.extend([5, 6])  # Add multiple
numbers.remove(3)  # Remove value
popped = numbers.pop()  # Remove and return last
del numbers[0]  # Delete by index

# Information
length = len(numbers)  # Size
count = numbers.count(2)  # Count occurrences
index = numbers.index(5)  # Find position
exists = 3 in numbers  # Check membership

# Sorting
numbers.sort()  # Sort in place
sorted_nums = sorted(numbers)  # Return sorted copy
numbers.reverse()  # Reverse in place

# Iteration
for item in numbers:  # Iterate values
    for i, item in enumerate(numbers):  # With index
        pass

# Common operations
total = sum(numbers)  # Sum all elements
maximum = max(numbers)  # Find maximum
minimum = min(numbers)  # Find minimum
```

## Summary

**Key Concepts:**

1. **Lists** store ordered collections of elements
2. **Indexing** starts at 0, negative indices count from end
3. **Slicing** extracts sublists with `[start:stop:step]`
4. **Lists are mutable** - can be modified after creation
5. **Many built-in methods** - append, remove, sort, etc.
6. **List comprehensions** provide concise syntax for creating lists
7. **2D lists** represent matrices and tables

Lists are fundamental to Python programming and mastering them is essential for solving complex problems efficiently!
