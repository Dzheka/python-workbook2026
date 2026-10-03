# Repetition in Python - The while Loop

The `while` loop repeats as long as a condition is true.

## Basic Syntax

```python
while condition:
    # code to execute
    # (usually modify something to eventually make condition false)
```

## Example 1: Count from 1 to 5

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

## Example 2: Reading Until Sentinel Value

**Problem**: Read numbers from the user until they enter 0.

```python
num = int(input("Enter a number (0 to stop): "))
while num != 0:
    print(f"You entered: {num}")
    num = int(input("Enter a number (0 to stop): "))
print("Done!")
```

## When to Use `for` vs `while`

| Use `for` when:                              | Use `while` when:                            |
|----------------------------------------------|----------------------------------------------|
| You know the number of iterations in advance | You repeat based on a condition              |
| Iterating over a sequence (range, string)    | Reading input until a sentinel value         |
| Processing each element in a collection      | Continuing until a specific condition is met |
| Example: "Print 1 to 100"                    | Example: "Read until user enters 0"          |
