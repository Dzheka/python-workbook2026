# Lucky Tickets (Medium)

A bus ticket has a 6-digit number. A ticket is **lucky** if the sum of its
first three digits equals the sum of its last three digits: `123321` is lucky
because 1 + 2 + 3 = 3 + 2 + 1.

## Task

- Write a function `digit_sum(n)` that returns the sum of the digits of `n`
- Write a function `is_lucky(ticket)` that returns `True` if the ticket is
  lucky and `False` otherwise
- Read two integers `a` and `b` (100000 ≤ a ≤ b ≤ 999999)
- Print how many lucky tickets there are from `a` to `b`, both included

## Examples

**Example 1:**

```
100000
100100
```

```
3
```

**Example 2:**

```
100000
999999
```

```
50412
```
