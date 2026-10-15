# F-String Formatting Basics

Essential Python f-string formatting for beginner programming exercises.

## Basic F-String Syntax

| Usage              | Example                        | Output                  |
|--------------------|--------------------------------|-------------------------|
| Simple variable    | `f"Hello {name}"`              | `Hello Alice`           |
| Multiple variables | `f"{name} is {age} years old"` | `Alice is 25 years old` |

## Number Formatting

| Format    | Description       | Example            | Output    |
|-----------|-------------------|--------------------|-----------|
| `{n}`     | Value as-is       | `f"{3.14159}"`     | `3.14159` |
| `{n:.2f}` | 2 decimal places  | `f"{3.14159:.2f}"` | `3.14`    |
| `{n:.1f}` | 1 decimal place   | `f"{3.14159:.1f}"` | `3.1`     |
| `{n:.0f}` | No decimal places | `f"{3.14159:.0f}"` | `3`       |

## Common Exercise Patterns

| Use Case            | Example                           | Output               |
|---------------------|-----------------------------------|----------------------|
| Quadratic roots (2) | `f"2 roots: {root1} and {root2}"` | `2 roots: 2.5 and 3.0` |
| Quadratic roots (1) | `f"1 root: {root}"`               | `1 root: 2.5`        |
| Grade points        | `f"{gpa}"`                        | `3.7`                |
| BMI calculation     | `f"{bmi:.1f}"`                    | `22.5`               |

## Simple Expressions

| Operation               | Example                        | Output              |
|-------------------------|--------------------------------|---------------------|
| Addition                | `f"{a} + {b} = {a + b}"`       | `5 + 3 = 8`         |
| Division with precision | `f"{a} / {b} = {a/b:.2f}"`     | `5 / 3 = 1.67`      |
| Square                  | `f"Square of {a} is {a**2}"`   | `Square of 5 is 25` |
| Math functions          | `f"√{n} = {math.sqrt(n):.2f}"` | `√5 = 2.24`         |

## Debugging Format

| Format       | Example           | Output         |
|--------------|-------------------|----------------|
| `{var=}`     | `f"{value=}"`     | `value=42`     |
| `{expr=}`    | `f"{value * 2=}"` | `value * 2=84` |
| `{var=:.2f}` | `f"{pi=:.2f}"`    | `pi=3.14`      |
