# Square Root

Implement Newton's method to compute the square root of a number.

## Task
- Read a number x from the user
- Use Newton's method to compute the square root
- Display the approximation

## Newton's Method
Start with a guess of `x / 2`, then repeatedly improve it by averaging the
guess with `x / guess`:

`guess = (guess + x / guess) / 2`

Each step lands closer to √x. Repeat until the guess is good enough.

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
