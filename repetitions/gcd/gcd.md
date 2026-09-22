# Greatest Common Divisor

Find the greatest common divisor (GCD) of two positive integers.

## Task
- Read two positive integers n and m from the user
- Use the provided algorithm to find their GCD
- Display the result

## Algorithm
1. Initialize d to the smaller of m and n
2. While d does not evenly divide m OR d does not evenly divide n:
   - Decrease d by 1
3. Report d as the greatest common divisor

## Examples
**Example 1:**
```
12
8
```
```
The GCD is 4
```

**Example 2:**
```
48
18
```
```
The GCD is 6
```

**Example 3:**
```
17
19
```
```
The GCD is 1
```

## Logic
- Read two numbers `m` and `n`
- Initialize `d` to the smaller of `m` and `n`
- Loop while `d` doesn't divide both `m` and `n`:
  - Decrease `d` by 1
- `d` is the GCD
