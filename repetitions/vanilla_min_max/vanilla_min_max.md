# Vanilla Min and Max

Find the minimum and maximum values from user input without using lists.

## Task
- Read integers from the user until a blank line is entered
- Track the minimum and maximum values as you read them
- Display both the minimum and maximum values
- Do NOT use lists or built-in min/max functions

## Examples
**Example 1:**
```
5
12
3
8
15

```
```
Minimum: 3
Maximum: 15
```

**Example 2:**
```
-5
-2
-10
-1

```
```
Minimum: -10
Maximum: -1
```

## Logic
- Read the first value (check if blank)
- Initialize min and max to the first value
- Use a while loop to read remaining values
- Update min if current value is smaller
- Update max if current value is larger
