# Perfect Numbers (Medium)

A **proper divisor** of `n` is a divisor of `n` smaller than `n` itself. By
the sum of its proper divisors, a number is:

- **perfect** — the sum equals the number (6 = 1 + 2 + 3)
- **abundant** — the sum is greater than the number
- **deficient** — the sum is less than the number

## Task

- Write a function `sum_of_divisors(n)` that returns the sum of the proper
  divisors of `n`
- Write a function `classify(n)` that returns `"perfect"`, `"abundant"` or
  `"deficient"`
- Read two integers `a` and `b` (1 ≤ a ≤ b)
- For every number from `a` to `b`, print the number and its group
- At the end, print how many numbers fell into each group

## Examples

**Example 1:**

```
5
12
```

```
5 is deficient
6 is perfect
7 is deficient
8 is deficient
9 is deficient
10 is deficient
11 is deficient
12 is abundant
Perfect: 1, Abundant: 1, Deficient: 6
```
