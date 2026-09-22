# Number Pyramid

Create a pyramid pattern using numbers instead of asterisks.

## Task
- Read a positive integer `n` from the user (height of pyramid)
- Display a centered pyramid where each row shows consecutive numbers
- Row `i` should have numbers from 1 to i, centered

## Examples
**Example 1:**
```
5
```
```
    1
   121
  12321
 1234321
123454321
```

**Example 2:**
```
3
```
```
  1
 121
12321
```

## Logic
- For each row i from 1 to n:
  - Print (n - i) spaces for centering
  - Print ascending numbers from 1 to i
  - Print descending numbers from (i-1) to 1
- Use nested loops to build each row
