# Geometric Sequence

Generate and display a geometric sequence.

## Task
- Read three values from the user:
  - `start`: first term of the sequence (float)
  - `ratio`: common ratio between consecutive terms (float)
  - `count`: number of terms to generate (integer)
- Display the first `count` terms of the geometric sequence
- Each term on its own line
- **Formatting:** Display whole numbers without decimal points (e.g., `100` instead of `100.0`), but show decimals when necessary (e.g., `12.5`)
- **Note:** You can assume that count is always at least 1

## Examples
**Example 1:**
```
2
3
5
```
```
2
6
18
54
162
```

**Example 2:**
```
100
0.5
5
```
```
100
50
25
12.5
6.25
```

## Logic
- Start with the first term
- Use a for loop to generate `count` terms
- Multiply by `ratio` to get the next term
- Display each term using 9 significant figures precision (use `:.9g` in f-string)
