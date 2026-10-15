# 3-Digit Palindrome

Write a program that determines if a `3-digit` integer is a palindrome.

## Examples

**Example 1:**

```
121
```

```
palindrome
```

**Example 2:**

```
123
```

```
not palindrome
```

**Example 3:**

```
505
```

```
palindrome
```

## Algorithm

For a `3-digit` number `ABC`:
- Extract digits: `A = n // 100`, `B = (n // 10) % 10`, `C = n % 10`
- Check if `A == C`
- If first digit equals last digit, it's a palindrome

## Note

- Assume input is always a `3-digit` number (`100-999`)
- A palindrome reads the same forwards and backwards
- Use integer division (`//`) and modulus (`%`) to extract digits
