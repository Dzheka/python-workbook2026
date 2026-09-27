# Number Triangle

Create a right triangle pattern using consecutive numbers.

## Task
- Read a positive integer `n` from the user
- Display a right triangle with `n` rows
- Each row `i` should contain numbers from 1 to i

## Examples
**Example 1:**
```
5
```
```
1
12
123
1234
12345
```

**Example 2:**
```
3
```
```
1
12
123
```

**Example 3:**
```
7
```
```
1
12
123
1234
12345
123456
1234567
```

## Logic
- Use nested loops: outer for rows (1 to n)
- For each row i:
  - Inner loop from 1 to i
  - Print each number without spaces
- Print newline after each row
