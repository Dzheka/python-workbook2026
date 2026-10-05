# Square Root

Implement Newton's method to compute the square root of a number.

## Task
- Read a number x from the user
- Use Newton's method to compute the square root
- Display the approximation

## Newton's Method Algorithm
1. Read x from the user
2. Initialize guess to x/2
3. While guess is not good enough:
   - Update guess to be the average of guess and x/guess
4. Display the result

## "Good Enough" Definition
A guess is good enough when:
- |guess² - x| ≤ 10⁻¹²

## Examples
**Example 1:**
```
16
```
```
4.0
```

**Example 2:**
```
2
```
```
1.414213562373095
```

**Example 3:**
```
100
```
```
10.0
```

## Logic
- Initialize `guess = x / 2`
- Loop while `abs(guess * guess - x) > 1e-12`:
  - `guess = (guess + x/guess) / 2`
- Display the final guess
