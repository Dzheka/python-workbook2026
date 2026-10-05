# Functions in Python - Best Practices and Quick Reference

## Best Practices

### 1. Function Naming

Use descriptive names that indicate what the function does:

```python
# Good
def calculate_area(length, width):
    return length * width

def is_valid_email(email):
    return "@" in email

# Poor
def calc(l, w):
    return l * w

def check(e):
    return "@" in e
```

**Naming conventions:**
- Use lowercase with underscores: `calculate_area`
- Start boolean functions with `is_`, `has_`, `can_`: `is_even`, `has_permission`
- Use verbs for actions: `calculate`, `convert`, `validate`
- Be specific: `get_user_age` not just `get_data`

### 2. Single Responsibility

Each function should do one thing well:

```python
# Good - each function has one responsibility
import math

def get_radius():
    return float(input("Enter radius: "))

def calculate_area(radius):
    return math.pi * radius ** 2

def display_result(area):
    print(f"Area: {area:.2f}")

# Usage
radius = get_radius()
area = calculate_area(radius)
display_result(area)

# Poor - one function does everything
import math

def do_everything():
    radius = float(input("Enter radius: "))
    area = math.pi * radius ** 2
    print(f"Area: {area:.2f}")
```

### 3. Keep Functions Short

Aim for functions that fit on one screen (typically 10-20 lines):

```python
# Good - broken into smaller functions
def is_strong_password(password):
    return (has_minimum_length(password) and
            has_uppercase(password) and
            has_digit(password))

def has_minimum_length(password):
    return len(password) >= 8

def has_uppercase(password):
    return any(c.isupper() for c in password)

def has_digit(password):
    return any(c.isdigit() for c in password)
```

### 4. Avoid Side Effects

Functions should avoid changing the global state:

```python
# Good - pure function (no side effects)
def add(a, b):
    return a + b

# Poor - modifies global variable
total = 0
def add_to_total(value):
    global total
    total += value
```

### 5. Use Type Hints

Make your function expectations clear:

```python
# Good - clear expectations
def calculate_discount(price: float, discount_percent: float) -> float:
    return price * (1 - discount_percent / 100)

# Less clear
def calculate_discount(price, discount):
    return price * (1 - discount / 100)
```

### 6. Document Complex Functions

Use docstrings for non-trivial functions:

```python
import math

def normalize_fraction(numerator: int, denominator: int) -> tuple:
    """
    Reduce a fraction to its simplest form.

    Parameters:
        numerator: The top number of the fraction
        denominator: The bottom number of the fraction

    Returns:
        A tuple (num, denom) in the simplest form

    Example:
        normalize_fraction(6, 9) returns (2, 3)
    """
    gcd = math.gcd(numerator, denominator)
    return numerator // gcd, denominator // gcd
```

### 7. Return Early for Validation

Handle edge cases early with early returns:

```python
# Good - early return
def divide(a, b):
    if b == 0:
        return None  # or raise an exception
    return a / b

# Poor - nested conditions
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return None
```

## When to Create a Function

Create a function when:

1. **You repeat code** - If you're copying and pasting code, make it a function
2. **Code is complex** - Break complex logic into named functions
3. **You need to test** - Functions make testing easier
4. **Code has a clear purpose** - Any operation with a clear purpose deserves a function
5. **You want to reuse logic** - Functions enable reusability

```python
# Without functions - repetitive
radius1 = 5
area1 = 3.14159 * radius1 ** 2
print(f"Circle 1 area: {area1}")

radius2 = 10
area2 = 3.14159 * radius2 ** 2
print(f"Circle 2 area: {area2}")

# With function - reusable and clear
import math

def calculate_circle_area(radius: float) -> float:
    return math.pi * radius ** 2

print(f"Circle 1 area: {calculate_circle_area(5)}")
print(f"Circle 2 area: {calculate_circle_area(10)}")
```

## Quick Reference

| Concept           | Syntax                       | Example                           |
|-------------------|------------------------------|-----------------------------------|
| Define function   | `def name():`                | `def greet():`                    |
| With parameters   | `def name(param):`           | `def greet(name):`                |
| With return       | `def name(): return value`   | `def add(a, b): return a + b`     |
| Default parameter | `def name(param=default):`   | `def greet(name="World"):`        |
| Type hints        | `def name(p: type) -> type:` | `def add(a: int, b: int) -> int:` |
| Call function     | `name()`                     | `greet()`                         |
| Call with args    | `name(arg1, arg2)`           | `add(3, 5)`                       |
| Multiple returns  | `return val1, val2`          | `return area, perimeter`          |
| Unpack returns    | `a, b = function()`          | `area, perim = calculate()`       |
| Docstring         | `"""Description"""`          | `"""Calculate sum."""`            |
| Local variable    | Variable inside function     | `x = 10` in function              |
| Global access     | `global var_name`            | `global counter`                  |
