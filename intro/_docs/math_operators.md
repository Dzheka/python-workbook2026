# Arithmetic Operators in Python

Arithmetic operators allow you to perform mathematical operations on numbers. These operators are essential for calculations in programming.

## The Arithmetic Operators

| Operator | Name           | Explanation                                         |
|----------|----------------|-----------------------------------------------------|
| `+`      | Addition       | Adds two numbers together                           |
| `-`      | Subtraction    | Subtracts the right number from the left number     |
| `*`      | Multiplication | Multiplies two numbers                              |
| `/`      | Division       | Divides left number by right number (returns float) |
| `//`     | Floor Division | Divides and rounds down to nearest integer          |
| `%`      | Modulo         | Returns the remainder after division                |
| `**`     | Exponentiation | Raises left number to the power of right number     |

## Examples

| Operator | Example                            | Result                  |
|----------|------------------------------------|-------------------------|
| `+`      | `5 + 3`<br>`2.5 + 1.5`<br>`10 + 0` | `8`<br>`4.0`<br>`10`    |
| `-`      | `5 - 3`<br>`10 - 7`<br>`3 - 5`     | `2`<br>`3`<br>`-2`      |
| `*`      | `5 * 3`<br>`4 * 2.5`<br>`7 * 0`    | `15`<br>`10.0`<br>`0`   |
| `/`      | `10 / 2`<br>`7 / 2`<br>`15 / 3`    | `5.0`<br>`3.5`<br>`5.0` |
| `//`     | `10 // 3`<br>`7 // 2`<br>`15 // 4` | `3`<br>`3`<br>`3`       |
| `%`      | `10 % 3`<br>`7 % 2`<br>`15 % 4`    | `1`<br>`1`<br>`3`       |
| `**`     | `2 ** 3`<br>`5 ** 2`<br>`10 ** 0`  | `8`<br>`25`<br>`1`      |

## Order of Operations (PEMDAS)

Python follows the standard mathematical order of operations:

1. **P**arentheses `()`
2. **E**xponents `**`
3. **M**ultiplication `*`, **D**ivision `/`, `//`, and Modulo `%`
4. **A**ddition `+` and **S**ubtraction `-`

| Expression      | Calculation   | Result |
|-----------------|---------------|--------|
| `2 + 3 * 4`     | `2 + (3 * 4)` | `14`   |
| `(2 + 3) * 4`   | `5 * 4`       | `20`   |
| `10 - 2 ** 3`   | `10 - 8`      | `2`    |
| `(10 - 2) ** 2` | `8 ** 2`      | `64`   |

## Common Use Cases

### Basic calculations
```python
a = 10
b = 3
sum_result = a + b        # 13
difference = a - b        # 7
product = a * b           # 30
quotient = a / b          # 3.333...
```

### Time and unit conversions
```python
total_seconds = 125
minutes = total_seconds // 60    # 2
remaining_seconds = total_seconds % 60  # 5
```

### Area calculations
```python
# Rectangle
length = 5
width = 3
area = length * width     # 15

# Circle
radius = 4
pi = 3.14159
area = pi * radius ** 2   # 50.26544
```
