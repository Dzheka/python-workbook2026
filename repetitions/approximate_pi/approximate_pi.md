# Approximate π

Approximate the value of π using an infinite series.

## Task
- Display 15 approximations of π
- Each approximation includes one more term from the series
- Use the following infinite series:

`π ≈ 3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8) - 4/(8×9×10) + 4/(10×11×12) - ...`

## Example Output
```
Approximation 1: 3.0
Approximation 2: 3.166666666666667
Approximation 3: 3.1333333333333337
Approximation 4: 3.1452380952380955
...
```

## Logic
- Start with `π ≈ 3`
- For each term (1 to 15):
  - Calculate denominator: `n × (n+1) × (n+2)` where `n` increases by 2 each time
  - Alternate between adding and subtracting `4/denominator`
  - Display the approximation

## Pattern
- Term 1: `3`
- Term 2: `3 + 4/(2×3×4)`
- Term 3: `3 + 4/(2×3×4) - 4/(4×5×6)`
- Term 4: `3 + 4/(2×3×4) - 4/(4×5×6) + 4/(6×7×8)`
