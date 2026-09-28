# Average

Write a program that computes the average of a collection of values entered by the user.

## Task
- Read values from the user until 0 is entered (sentinel value)
- Compute the average of all values (excluding the 0)
- Display the average

## Examples
**Example 1:**
```
10
20
30
0
```
```
The average is 20.0
```

**Example 2:**
```
5
15
25
35
0
```
```
The average is 20.0
```

## Logic
- Use a while loop to read values until 0 is entered
- Keep track of the `sum` and `count` of values
- The 0 should not be included in the average
- Average = `sum / count`
