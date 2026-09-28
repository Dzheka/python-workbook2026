# Prime Factors

Find and display the prime factorization of an integer.

## Task
- Read an integer from the user
- If the value is less than 2, display an error message
- Otherwise, display the prime factors (one per line)

## Algorithm
1. Initialize factor to 2
2. While factor ≤ n:
   - If n is evenly divisible by factor:
     - Display factor (it's a prime factor)
     - Divide n by factor (floor division)
   - Else:
     - Increase factor by 1

## Examples
**Example 1:**
```
72
```
```
The prime factors of 72 are:
2
2
2
3
3
3
```

**Example 2:**
```
17
```
```
The prime factors of 17 are:
17
```

**Example 3:**
```
1
```
```
Error: Number must be 2 or greater
```

## Logic
- Prime factorization breaks a number into prime numbers that multiply to give the original
- Read integer `n`
- Start with `factor = 2`
- Keep dividing by current `factor` while divisible
- When not divisible, increment `factor`
- Continue until `factor > n`
