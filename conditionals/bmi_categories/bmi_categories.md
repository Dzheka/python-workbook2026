# BMI Categories

Write a program that calculates `BMI` and determines the weight category.

## BMI Categories

| BMI Range           | Category      |
|---------------------|---------------|
| `BMI < 18.5`        | Underweight   |
| `18.5 ≤ BMI < 25.0` | Normal weight |
| `25.0 ≤ BMI < 30.0` | Overweight    |
| `BMI ≥ 30.0`        | Obese         |

## Examples

**Example 1:**

```
70
1.75
```

```
Normal weight
```

**Example 2:**

```
50
1.70
```

```
Underweight
```

**Example 3:**

```
85
1.75
```

```
Overweight
```

**Example 4:**

```
100
1.75
```

```
Obese
```

**Example 5:**

```
60
1.60
```

```
Normal weight
```

## Formula

`BMI = weight (kg) / height² (m²)`

## Note

- Calculate `BMI` first, then categorize
- Use appropriate comparison operators for ranges
- Weight in kilograms, height in meters
- Standard WHO `BMI` categories
