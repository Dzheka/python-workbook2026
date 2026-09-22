# Digit Sum

Calculate the sum of all digits in an integer using loops.

## Task
- Read an integer from the user
- Calculate the sum of its digits using a loop
- Display the sum
- Negative numbers: sum their digits (ignore the minus sign)

## Examples
**Example 1:**
```
12345
```
```
15
```

**Example 2:**
```
-987
```
```
24
```

**Example 3:**
```
0
```
```
0
```

## Logic
- Take the absolute value to handle negative numbers
- Initialize sum to 0
- Use a while loop:
  - While number > 0:
    - Add the last digit (number % 10) to sum
    - Remove the last digit (number // 10)
- Display the sum
