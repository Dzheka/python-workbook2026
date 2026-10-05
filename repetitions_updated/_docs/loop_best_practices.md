# Repetition in Python - Best Practices and Quick Reference

## Common Pitfalls

### 1. Infinite Loops

Make sure your loop condition will eventually become false:

```python
# WRONG - Infinite loop!
i = 1
while i <= 5:
    print(i)
    # Forgot to increment i!

# CORRECT
i = 1
while i <= 5:
    print(i)
    i += 1
```

### 2. Off-by-One Errors

Be careful with loop boundaries:

```python
# To print 1 to 10 (inclusive)
for i in range(1, 11):  # NOT range(1, 10)
    print(i)
```

### 3. Modifying Loop Variable in For Loop

Avoid modifying the loop variable inside a `for` loop:

```python
# WRONG - Don't modify i inside the loop
for i in range(5):
    print(i)
    i += 1  # This doesn't affect the loop!

# Use a while loop if you need to control the increment
```

## Quick Reference

| Operation                   | Example                           | Description                    |
|-----------------------------|-----------------------------------|--------------------------------|
| For loop (count)            | `for i in range(10):`             | Loop 10 times (0 to 9)         |
| For loop (start, stop)      | `for i in range(5, 10):`          | Loop from 5 to 9               |
| For loop (with step)        | `for i in range(0, 10, 2):`       | Loop 0, 2, 4, 6, 8             |
| For loop (backwards)        | `for i in range(10, 0, -1):`      | Loop 10, 9, 8, ..., 1          |
| While loop                  | `while condition:`                | Loop while condition is True   |
| Iterate string              | `for char in text:`               | Process each character         |
| Loop with index             | `for i in range(len(text)):`      | Access by index                |
| Loop with index (better)    | `for i, char in enumerate(text):` | Access index and value         |
| Break out of loop           | `break`                           | Exit loop immediately          |
| Skip to next iteration      | `continue`                        | Skip rest of current iteration |
| Infinite loop (be careful!) | `while True:`                     | Loop forever (use with break)  |
| Accumulate sum              | `total += value`                  | Add to running total           |
| Count occurrences           | `count += 1`                      | Increment counter              |

## Tips for Success

Loops are essential for writing programs that process large amounts of data or
repeat tasks.

1. **Choose the right loop**: Use `for` when you know the count, `while` for
   conditions
2. **Initialize before the loop**: Set up accumulators, counters, and other
   variables
3. **Update inside the loop**: Make sure loop variables change to avoid infinite
   loops
4. **Test loop boundaries**: Verify your loop runs the correct number of times
5. **Use descriptive variable names**: `row`, `column`, `total` are better than
   `i`, `j`, `x`
6. **Indent properly**: Python requires correct indentation for loop bodies
7. **Debug with print statements**: Add `print()` to see what's happening in
   each iteration
