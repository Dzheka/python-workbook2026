# Arithmetic Sequence

Generate and display an arithmetic sequence.

## Task
- Read three integers from the user:
  - `start`: first term of the sequence
  - `diff`: common difference between consecutive terms
  - `count`: number of terms to generate
- Display all terms of the arithmetic sequence
- Each term on its own line
- **Note:** You can assume that the inputs are always valid (count is positive)

## Examples
**Example 1:**
```
5
3
6
```
```
5
8
11
14
17
20
```

**Example 2:**
```
10
-2
5
```
```
10
8
6
4
2
```

**Note:** Since inputs are guaranteed to be valid, there are no error cases to consider.

## Logic
- Start with the first term
- Use a loop to generate exactly `count` terms
- Add `diff` to get the next term after each iteration
