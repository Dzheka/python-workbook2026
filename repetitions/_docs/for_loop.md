# Repetition in Python - The for Loop

## Introduction

In the previous chapters, you worked with sequential programs and programs that
use conditional statements to make
decisions.
While these constructs are powerful, many interesting problems require executing
the same code multiple times. For
example:

- Printing a pattern with 100 rows
- Reading values until the user enters a specific value
- Processing each character in a string
- Finding the sum of numbers from 1 to 1000

Writing the same code repeatedly would be impractical and error-prone. **Loops**
allow you to execute a block of code
multiple times efficiently.

## The Two Types of Loops

Python provides two main types of loops:

1. **`for` loop** - Used when you know how many times to repeat
2. **`while` loop** - Used when you repeat based on a condition

## The `for` Loop

The `for` loop is used to iterate over a sequence (like a range of numbers, a
string, or a list).

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

## The `range()` Function

The `range()` function generates a sequence of numbers and is commonly used with
for loops.

| Usage                      | Description                  | Example            | Generated Values   |
|----------------------------|------------------------------|--------------------|--------------------|
| `range(stop)`              | From 0 to stop-1             | `range(5)`         | `0, 1, 2, 3, 4`    |
| `range(start, stop)`       | From start to stop-1         | `range(2, 6)`      | `2, 3, 4, 5`       |
| `range(start, stop, step)` | From start to stop-1 by step | `range(1, 10, 2)`  | `1, 3, 5, 7, 9`    |
| Backwards                  | Using negative step          | `range(10, 0, -1)` | `10, 9, 8, ..., 1` |

## Range Examples

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

## Useful `print()` Parameters

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
# sep separates multiple arguments in a single print call
print(1, 2, 3, 4, 5, sep="-")
# Output: 1-2-3-4-5
```
