# Repetition in Python - Common Loop Patterns

The following are common patterns you'll use repeatedly when working with loops.

## Pattern 1: Accumulation (Sum/Total)

Calculate the sum of numbers from 1 to 10:

```python
total = 0
for i in range(1, 11):
    total += i
print(f"Sum: {total}")  # Sum: 55
```

## Pattern 2: Counting

Count how many even numbers are between 1 and 10:

```python
count = 0
for i in range(1, 11):
    if i % 2 == 0:
        count += 1
print(f"Even numbers: {count}")  # Even numbers: 5
```

## Pattern 3: Finding Maximum/Minimum

Find the maximum of numbers entered by the user:

```python
max_value = float('-inf')  # Start with very small value
for i in range(5):
    num = int(input("Enter a number: "))
    if num > max_value:
        max_value = num
print(f"Maximum: {max_value}")
```

> **Note:** For minimum, use `float('inf')` instead.
