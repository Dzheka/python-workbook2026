# Exercise: The Bill (Quiz Q10)

Read three values with three `input()` calls — the price of one item, the
quantity, and the discount in percent — then print three lines:

```
subtotal   45.50
discount    2.73
total      42.77
```

- `subtotal` = price × quantity
- `discount` = the given percent of the subtotal
- `total` = subtotal − discount

Formatting: the label is 10 characters wide and left-aligned, the value is
6 wide, right-aligned, with 2 decimals.

Hint: `f"{label:<10}{value:>6.2f}"`

Compute the discount from the full subtotal, never from an already rounded
number.

## Examples

**Example 1:**

```
6.5
7
6
```

```
subtotal   45.50
discount    2.73
total      42.77
```

**Example 2:**

```
10.00
3
15
```

```
subtotal   30.00
discount    4.50
total      25.50
```

**Example 3:**

```
4.25
8
0
```

```
subtotal   34.00
discount    0.00
total      34.00
```
