# 4-Digit Palindrome

Write a program that determines if a `4-digit` integer is a palindrome.

## Examples

**Example 1:**

```
1221
```

```
palindrome
```

**Example 2:**

```
1234
```

```
not palindrome
```

**Example 3:**

```
9009
```

```
palindrome
```

**Example 4:**

```
7337
```

```
palindrome
```

**Example 5:**

```
5678
```

```
not palindrome
```

## Algorithm

For a `4-digit` number `ABCD`:
- Extract digits:
  - `A = n // 1000`
  - `B = (n // 100) % 10`
  - `C = (n // 10) % 10`
  - `D = n % 10`
- Check if `A == D` and `B == C`
- If first equals last AND second equals third, it's a palindrome

## Note

- Assume input is always a `4-digit` number (`1000-9999`)
- A palindrome reads the same forwards and backwards
- Use integer division (`//`) and modulus (`%`) to extract digits
- Both outer digits AND inner digits must match
