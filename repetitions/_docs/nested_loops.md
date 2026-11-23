# Repetition in Python - Nested Loops

A loop inside another loop is called a **nested loop**. The inner loop executes
completely for each iteration of the
outer loop.

## Example: Triangle of Numbers

```python
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
```

**Output (for n = 4):**

```
1
1 2
1 2 3
1 2 3 4
```
