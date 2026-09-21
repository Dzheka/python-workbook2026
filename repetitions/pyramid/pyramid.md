# Pyramid Art

Create a centered pyramid pattern using asterisks.

## Task
- Read a positive integer `n` from the user (height of pyramid)
- Display a centered pyramid with `n` rows
- Row `i` should have `2*i - 1` asterisks centered

## Examples
**Example 1:**
```
5
```
```
    *
   ***
  *****
 *******
*********
```

**Example 2:**
```
3
```
```
  *
 ***
*****
```

## Logic
- For each row i from 1 to n:
  - Number of spaces = n - i
  - Number of stars = 2 * i - 1
  - Print: spaces + stars
