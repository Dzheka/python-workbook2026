# No More Pennies

Canadian retailers must round cash payments to the nearest nickel (5 cents).

## Task
- Read prices from the user until a blank line is entered
- Calculate the total cost
- Calculate the cash payment amount (rounded to nearest nickel)
- Display both the total and the cash payment amount

## Examples
**Example 1:**
```
10.25
5.78
3.12

```
```
Total: $19.15
Cash payment: $19.15
```

**Example 2:**
```
4.99
2.48
1.22

```
```
Total: $8.69
Cash payment: $8.70
```

**Example 3:**
```
7.53
3.21

```
```
Total: $10.74
Cash payment: $10.75
```

## Logic
- Use a while loop to read prices until blank line
- Sum all prices for total
- For cash payment:
  - Convert total to pennies `total × 100`
  - Find remainder when divided by 5
  - If remainder < 2.5: round down
  - Otherwise: round up
