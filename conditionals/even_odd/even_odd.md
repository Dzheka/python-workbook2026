# Even or Odd?

Write a program that reads an integer from the user and determines whether the integer is `even` or `odd`.

## Examples

**Example 1:**

```
7
```

```
odd
```

**Example 2:**

```
4
```

```
even
```

**Example 3:**

```
0
```

```
even
```

**Example 4:**

```
-3
```

```
odd
```

## Logic

- If `number % 2 == 0`: even
- If `number % 2 != 0`: odd

## Note

- Zero is considered even
- The modulo operator `%` returns the remainder of division
- Handle negative numbers (they follow the same rule)
