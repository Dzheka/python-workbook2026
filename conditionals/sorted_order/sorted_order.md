# Sorted Order

Write a program that determines if three numbers are sorted in ascending order, descending order, equal, or random order.

## Examples

**Example 1:**

```
1
5
9
```

```
ascending
```

**Example 2:**

```
9
5
1
```

```
descending
```

**Example 3:**

```
5
1
9
```

```
random
```

**Example 4:**

```
3
3
7
```

```
ascending
```

**Example 5:**

```
8
4
4
```

```
descending
```

**Example 6:**

```
2
2
2
```

```
equal
```

## Logic

- **Equal**: a == b == c (all three numbers are the same)
- **Ascending**: a ≤ b ≤ c (and not all equal)
- **Descending**: a ≥ b ≥ c (and not all equal)
- **Random**: neither ascending, descending, nor equal

## Note

- Check for all equal first as a special case
- Allow equal adjacent values for ascending/descending (non-strict ordering)
