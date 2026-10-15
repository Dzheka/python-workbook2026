# Valid Triangle

Write a program that determines if three side lengths can form a valid triangle.

## Triangle Inequality Theorem

For sides `a`, `b`, and `c` to form a valid triangle:

- `a + b > c`
- `a + c > b`
- `b + c > a`

All three conditions must be true.

## Examples

**Example 1:**

```
3
4
5
```

```
valid triangle
```

**Example 2:**

```
1
2
5
```

```
invalid triangle
```

**Example 3:**

```
1
1
3
```

```
invalid triangle
```

## Note

- All sides must be positive
- The sum of any two sides must be greater than the third side
- Check all three combinations of the triangle inequality
- Use logical `AND` to combine all conditions
- Alternatively you can do `abs(a-c) < b < a+c`
