# Python Math Functions Reference

Complete guide to Python's mathematical functions and constants available in the `math` module and built-in functions.

## Importing the Math Module

```python
import math
```

## Built-in Mathematical Functions

These functions are available without importing any module:

| Function         | Description               | Example             | Result   |
|------------------|---------------------------|---------------------|----------|
| `abs(x)`         | Absolute value            | `abs(-5)`           | `5`      |
| `round(x)`       | Round to nearest integer  | `round(3.7)`        | `4`      |
| `round(x, n)`    | Round to n decimal places | `round(3.14159, 2)` | `3.14`   |
| `min(x, y, ...)` | Find minimum value        | `min(5, 2, 8, 1)`   | `1`      |
| `max(x, y, ...)` | Find maximum value        | `max(5, 2, 8, 1)`   | `8`      |
| `sum(iterable)`  | Sum of all elements       | `sum([1, 2, 3, 4])` | `10`     |
| `pow(x, y)`      | Power (same as x**y)      | `pow(2, 3)`         | `8`      |
| `pow(x, y, z)`   | Power with modulo         | `pow(2, 3, 5)`      | `3`      |
| `divmod(x, y)`   | Division and remainder    | `divmod(17, 5)`     | `(3, 2)` |

> **Note:** `round()` uses banker's rounding (half to even) — `round(2.5)` is
> `2`, `round(3.5)` is `4`. When an exercise requires a fixed number of
> decimal places in *output*, format with f-strings (`f"{x:.2f}"`) instead of `round()`.

## Basic Math Module Functions

| Function            | Description           | Example            | Result    |
|---------------------|-----------------------|--------------------|-----------|
| `math.sqrt(x)`      | Square root           | `math.sqrt(16)`    | `4.0`     |
| `math.pow(x, y)`    | Power (returns float) | `math.pow(2, 3)`   | `8.0`     |
| `math.exp(x)`       | e^x                   | `math.exp(1)`      | `2.71828` |
| `math.log(x)`       | Natural logarithm     | `math.log(math.e)` | `1.0`     |
| `math.log(x, base)` | Logarithm with base   | `math.log(8, 2)`   | `3.0`     |
| `math.log10(x)`     | Base-10 logarithm     | `math.log10(100)`  | `2.0`     |
| `math.log2(x)`      | Base-2 logarithm      | `math.log2(8)`     | `3.0`     |

## Trigonometric Functions

All angles are in **radians**. Use `math.radians()` to convert from degrees.

| Function           | Description                  | Example               | Result   |
|--------------------|------------------------------|-----------------------|----------|
| `math.sin(x)`      | Sine                         | `math.sin(math.pi/2)` | `1.0`    |
| `math.cos(x)`      | Cosine                       | `math.cos(0)`         | `1.0`    |
| `math.tan(x)`      | Tangent                      | `math.tan(math.pi/4)` | `1.0`    |
| `math.asin(x)`     | Arcsine (returns radians)    | `math.asin(1)`        | `1.5708` |
| `math.acos(x)`     | Arccosine (returns radians)  | `math.acos(0)`        | `1.5708` |
| `math.atan(x)`     | Arctangent (returns radians) | `math.atan(1)`        | `0.7854` |
| `math.atan2(y, x)` | Two-argument arctangent      | `math.atan2(1, 1)`    | `0.7854` |

## Angle Conversion

| Function          | Description        | Example                 | Result    |
|-------------------|--------------------|-------------------------|-----------|
| `math.radians(x)` | Degrees to radians | `math.radians(180)`     | `3.14159` |
| `math.degrees(x)` | Radians to degrees | `math.degrees(math.pi)` | `180.0`   |

## Rounding and Ceiling Functions

| Function        | Description               | Example            | Result |
|-----------------|---------------------------|--------------------|--------|
| `math.ceil(x)`  | Ceiling (round up)        | `math.ceil(3.14)`  | `4`    |
| `math.floor(x)` | Floor (round down)        | `math.floor(3.14)` | `3`    |
| `math.trunc(x)` | Truncate (remove decimal) | `math.trunc(3.14)` | `3`    |

## Special Functions

| Function              | Description                         | Example             | Result |
|-----------------------|-------------------------------------|---------------------|--------|
| `math.factorial(x)`   | Factorial (x!)                      | `math.factorial(5)` | `120`  |
| `math.gcd(x, y)`      | Greatest common divisor             | `math.gcd(12, 8)`   | `4`    |
| `math.lcm(x, y, ...)` | Least common multiple (Python 3.9+) | `math.lcm(12, 8)`   | `24`   |
| `math.isqrt(x)`       | Integer square root (Python 3.8+)   | `math.isqrt(15)`    | `3`    |

## Classification Functions

| Function             | Description             | Example                      | Result |
|----------------------|-------------------------|------------------------------|--------|
| `math.isfinite(x)`   | Check if finite         | `math.isfinite(1.0)`         | `True` |
| `math.isinf(x)`      | Check if infinite       | `math.isinf(float('inf'))`   | `True` |
| `math.isnan(x)`      | Check if NaN            | `math.isnan(float('nan'))`   | `True` |
| `math.isclose(a, b)` | Check if close in value | `math.isclose(0.1+0.2, 0.3)` | `True` |

## Mathematical Constants

| Constant   | Value         | Description        |
|------------|---------------|--------------------|
| `math.pi`  | 3.14159265... | Pi (π)             |
| `math.e`   | 2.71828182... | Euler's number (e) |
| `math.tau` | 6.28318530... | Tau (2π)           |
| `math.inf` | inf           | Positive infinity  |
| `math.nan` | nan           | Not a Number       |
