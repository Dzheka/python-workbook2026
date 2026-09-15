# Between Values

Write a program that determines if a value `b` is between two other values `a` and `c`.

## Examples

**Example 1:**

```
5
7
10
```

```
between
```

**Example 2:**

```
10
7
5
```

```
between
```

**Example 3:**

```
5
12
10
```

```
not between
```

**Example 4:**

```
5
5
10
```

```
between
```

**Example 5:**

```
10
5
5
```

```
between
```

## Logic

- If `a ≤ c`: check if `a ≤ b ≤ c`
- If `a > c`: check if `c ≤ b ≤ a`
- Use inclusive comparison (`≤` and `≥`)

## Note

- Handle both ascending and descending ranges
- Include boundary values (`b` can equal `a` or `c`)
- The order of `a` and `c` doesn't matter for determining the range
