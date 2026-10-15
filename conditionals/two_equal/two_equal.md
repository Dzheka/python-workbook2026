# Two Equal

Write a program that determines if at least two of three integers are equal.

## Examples

**Example 1:**

```
5
5
3
```

```
yes
```

**Example 2:**

```
1
2
3
```

```
no
```

**Example 3:**

```
7
3
7
```

```
yes
```

**Example 4:**

```
4
4
4
```

```
yes
```

**Example 5:**

```
9
2
9
```

```
yes
```

## Logic

Check if any of the three pairs are equal:
- `a == b` OR `a == c` OR `b == c`

## Note

- At least two must be equal (can be all three)
- Handle all possible arrangements of equal pairs
- Use logical OR to combine conditions
