# Number of Digits

Count the number of digits in an integer using loops.

## Task
- Read an integer from the user
- Count the number of digits using a loop (not using len() or string conversion)
- Display the count
- Negative numbers should count their digits (ignore the minus sign)

## Examples
**Example 1:**
```
12345
```
```
5
```

**Example 2:**
```
-987
```
```
3
```

**Example 3:**
```
0
```
```
1
```

## Logic
- Take the absolute value to handle negative numbers
- Initialize count to 0
- Use a while loop:
  - While number > 0:
    - Increment count
    - Divide number by 10 (integer division)
- Special case: if input is 0, return 1
