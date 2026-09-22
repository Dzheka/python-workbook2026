# Repetition Structures in Python

## Introduction

In the previous chapters, you worked with sequential programs and programs that use conditional statements to make
decisions.
While these constructs are powerful, many interesting problems require executing the same code multiple times. For
example:

- Printing a pattern with 100 rows
- Reading values until the user enters a specific value
- Processing each character in a string
- Finding the sum of numbers from 1 to 1000

Writing the same code repeatedly would be impractical and error-prone. **Loops** allow you to execute a block of code
multiple times efficiently.

## The Two Types of Loops

Python provides two main types of loops:

1. **`for` loop** - Used when you know how many times to repeat
2. **`while` loop** - Used when you repeat based on a condition

## The `for` Loop

The `for` loop is used to iterate over a sequence (like a range of numbers, a string, or a list).

### Basic Syntax

```python
for variable in sequence:
# code to execute
```

### Example: Counting from 1 to 5

```python
for i in range(1, 6):
    print(i)
```

**Output:**

```
1
2
3
4
5
```

### The range() Function

The `range()` function generates a sequence of numbers and is commonly used with for loops.

| Usage                      | Description                  | Example            | Generated Values   |
|----------------------------|------------------------------|--------------------|--------------------|
| `range(stop)`              | From 0 to stop-1             | `range(5)`         | `0, 1, 2, 3, 4`    |
| `range(start, stop)`       | From start to stop-1         | `range(2, 6)`      | `2, 3, 4, 5`       |
| `range(start, stop, step)` | From start to stop-1 by step | `range(1, 10, 2)`  | `1, 3, 5, 7, 9`    |
| Backwards                  | Using negative step          | `range(10, 0, -1)` | `10, 9, 8, ..., 1` |

### Range Examples

```python
# Count 0 to 4
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Count 1 to 10
for i in range(1, 11):
    print(i)  # 1, 2, 3, ..., 10

# Count by 10s from 0 to 100
for i in range(0, 101, 10):
    print(i)  # 0, 10, 20, ..., 100

# Count backwards from 5 to 1
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

## Iterating Over Strings

You can iterate over each character in a string:

```python
word = "hello"
for char in word:
    print(char)
```

**Output:**

```
h
e
l
l
o
```

## The `while` Loop

The `while` loop repeats as long as a condition is true.

### Basic Syntax

```python
while condition:
# code to execute
# (usually modify something to eventually make condition false)
```

### Example 1: Count from 1 to 5

```python
count = 1
while count <= 5:
    print(count)
    count += 1  # Increment count
```

**Output:**

```
1
2
3
4
5
```

### Example 2: Reading Until Sentinel Value

**Problem**: Read numbers from the user until they enter 0.

```python
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    print(f"You entered: {num}")
    num = int(input("Enter a number (0 to stop): "))
print("Done!")
```

## Common Loop Patterns

### Pattern 1: Accumulation (Sum/Total)

Calculate the sum of numbers from 1 to 10:

```python
total = 0
for i in range(1, 11):
    total += i
print(f"Sum: {total}")  # Sum: 55
```

### Pattern 2: Counting

Count how many even numbers are between 1 and 10:

```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
print(f"Even numbers: {count}")  # Even numbers: 5
```

### Pattern 3: Finding Maximum/Minimum

Find the maximum of numbers entered by the user:

```python
max_value = float('-inf')  # Start with very small value
for i in range(5):
    num = int(input("Enter a number: "))
    if num > max_value:
        max_value = num
print(f"Maximum: {max_value}")
```

## Nested Loops

A loop inside another loop is called a **nested loop**. The inner loop executes completely for each iteration of the
outer loop.

### Example 1: Triangle of Numbers

```python
n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
```

## Loop Control Statements

### `break` - Exit the Loop Early

The `break` statement immediately exits the loop:

```python
# Find first number divisible by 7 between 100 and 200
for i in range(100, 201):
    if i % 7 == 0:
        print(f"Found: {i}")
        break  # Exit loop
```

### `continue` - Skip to Next Iteration

The `continue` statement skips the rest of the current iteration and moves to the next:

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

## Using `print()` with Loops

### Printing on the Same Line

Use `end=""` parameter to prevent newline:

```python
# Print numbers on one line
for i in range(1, 6):
    print(i, end=" ")  # Print with space separator
print()  # Newline at the end
# Output: 1 2 3 4 5
```

### Using sep Parameter

```python
# Print with custom separator
for i in range(1, 6):
    print(i, sep="-")
print()
# Output: 1-2-3-4-5-
```

## When to Use `for` vs `while`

| Use `for` when:                              | Use `while` when:                            |
|----------------------------------------------|----------------------------------------------|
| You know the number of iterations in advance | You repeat based on a condition              |
| Iterating over a sequence (range, string)    | Reading input until a sentinel value         |
| Processing each element in a collection      | Continuing until a specific condition is met |
| Example: "Print 1 to 100"                    | Example: "Read until user enters 0"          |

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

## Tips for Success

1. **Choose the right loop**: Use `for` when you know the count, `while` for conditions
2. **Initialize before the loop**: Set up accumulators, counters, and other variables
3. **Update inside the loop**: Make sure loop variables change to avoid infinite loops
4. **Test loop boundaries**: Verify your loop runs the correct number of times
5. **Use descriptive variable names**: `row`, `column`, `total` are better than `i`, `j`, `x`
6. **Indent properly**: Python requires correct indentation for loop bodies
7. **Debug with print statements**: Add `print()` to see what's happening in each iteration

## Quick Reference

| Operation                   | Example                      | Description                    |
|-----------------------------|------------------------------|--------------------------------|
| For loop (count)            | `for i in range(10):`        | Loop 10 times (0 to 9)         |
| For loop (start, stop)      | `for i in range(5, 10):`     | Loop from 5 to 9               |
| For loop (with step)        | `for i in range(0, 10, 2):`  | Loop 0, 2, 4, 6, 8             |
| For loop (backwards)        | `for i in range(10, 0, -1):` | Loop 10, 9, 8, ..., 1          |
| While loop                  | `while condition:`           | Loop while condition is True   |
| Iterate string              | `for char in text:`          | Process each character         |
| Loop with index             | `for i in range(len(text)):` | Access by index                |
| Break out of loop           | `break`                      | Exit loop immediately          |
| Skip to next iteration      | `continue`                   | Skip rest of current iteration |
| Infinite loop (be careful!) | `while True:`                | Loop forever (use with break)  |
| Get digit                   | `digit = n % 10`             | Extract last digit             |
| Remove digit                | `n = n // 10`                | Remove last digit              |
| Accumulate sum              | `total += value`             | Add to running total           |
| Count occurrences           | `count += 1`                 | Increment counter              |

## Summary

Loops are essential for writing programs that process large amounts of data or repeat tasks. The key concepts covered in
this chapter are:

- **For loops**: Iterate a specific number of times using `range()`
- **While loops**: Repeat based on a condition
- **Nested loops**: Loops within loops for multidimensional patterns
- **Loop control**: `break`, `continue`, and `else` clauses
- **Common patterns**: Accumulation, counting, sentinel values, digit processing

With loops, you can solve much more complex problems efficiently. Practice is key to mastering these concepts!
