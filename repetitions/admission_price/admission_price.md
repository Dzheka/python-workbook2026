# Admission Price

A zoo determines admission price based on the age of guests.

## Task
- Read ages of all guests in a group (one age per line)
- User enters blank line when done
- Calculate total admission cost
- Display the cost with 2 decimal places

## Pricing
- Age 2 and under: Free ($0.00)
- Age 3-12: $14.00
- Age 65 and over: $18.00
- All others: $23.00

## Examples
**Example 1:**
```
5
10
65
40

```
```
$69.00
```

**Example 2:**
```
2
8
35

```
```
$37.00
```

**Example 3:**
```
1
2
3

```
```
$14.00
```

## Logic
- Use a while loop to read ages until blank line
- For each age, determine price based on age category
- Add to running total
- Display total with 2 decimal places
