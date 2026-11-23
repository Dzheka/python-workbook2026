# Repetition in Python - break and continue

Loops can be controlled from within using the `break` and `continue` statements.

## `break` - Exit the Loop Early

The `break` statement immediately exits the loop:

```python
# Find first number divisible by 7 between 100 and 200
for i in range(100, 201):
    if i % 7 == 0:
        print(f"Found: {i}")
        break  # Exit loop
```

## `continue` - Skip to Next Iteration

The `continue` statement skips the rest of the current iteration and moves to
the next:

```python
# Print odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)
```

**Output:**

```
1
3
5
7
9
```

## `else` After Loops

- Python supports an `else` clause on loops that executes when the loop
  completes without hitting a `break`. While this
  feature exists, it's not commonly used and can be confusing since it's unique
  to Python and not available in most other
  programming languages. We recommend avoiding it for clarity.
