# Lists in Python - 2D Lists (Nested Lists)

## 2D Lists (Nested Lists)

### Creating 2D Lists

```python
# 3x3 matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Create 3x4 matrix of zeros
rows, cols = 3, 4
matrix0 = [[0 for _ in range(cols)] for _ in range(rows)]
```

### Accessing 2D List Elements

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0][0])  # 1 (row 0, col 0)
print(matrix[1][2])  # 6 (row 1, col 2)
print(matrix[2][1])  # 8 (row 2, col 1)
```

### Iterating 2D Lists

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Iterate rows and columns
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# With indices
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()
```

### Common Mistake: Creating 2D Lists Incorrectly

```python
# WRONG - creates references to the same list
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
