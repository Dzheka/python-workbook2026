# Creating Your Own Modules

## Introduction

You've learned how to import and use existing modules. Now it's time to learn how to **create your own modules** that others (or you) can import and reuse.

A **module** is simply a Python file containing functions, variables, and classes. Any `.py` file can be imported as a module!

## Why Create Modules?

- **Code organization**: Break large programs into manageable files
- **Reusability**: Use the same functions across multiple projects
- **Collaboration**: Share code with teammates
- **Maintainability**: Fix bugs in one place, benefit everywhere
- **Clarity**: Group related functionality together

## Creating a Simple Module

Creating a module is as simple as writing functions in a `.py` file:

**File: `geometry.py`**
```python
import math

def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

def rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return (base * height) / 2
```

That's it! You've created a module. Now you can import it in other files:

**File: `main.py`**
```python
import geometry

# Use functions from your module
circle = geometry.circle_area(5)
rect = geometry.rectangle_area(10, 20)
triangle = geometry.triangle_area(6, 8)

print(f"Circle area: {circle}")
print(f"Rectangle area: {rect}")
print(f"Triangle area: {triangle}")
```

## Import Your Own Module

There are multiple ways to import your own modules:

### Method 1: Import the entire module

```python
import geometry

area = geometry.circle_area(5)
```

### Method 2: Import specific functions

```python
from geometry import circle_area, rectangle_area

area = circle_area(5)
rect = rectangle_area(3, 4)
```

### Method 3: Import with alias

```python
import geometry as geo

area = geo.circle_area(5)
```

## Module Requirements

For a file to be importable as a module:

1. **Same directory**: The module file must be in the same directory as the file importing it (or in Python's path)
2. **Valid Python filename**: Use lowercase with underscores (e.g., `my_module.py`)
3. **No spaces**: Filename cannot have spaces
4. **Valid syntax**: The module must have valid Python code

## The Problem with Test Code

When you import a module, Python executes **all** the code in that file. This causes issues:

**File: `calculator.py`**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Testing code
print("Testing calculator...")
print(add(5, 3))      # 8
print(subtract(10, 4)) # 6
```

**File: `main.py`**
```python
import calculator  # This will run the test code!

result = calculator.add(100, 200)
print(result)
```

**Output:**
```
Testing calculator...
8
6
300
```

The test code runs automatically when we import! This is not what we want.

## The `if __name__ == "__main__"` Pattern

### How It Works

Python provides a special variable `__name__` that tells you how the file is being used:

- **Running directly**: `python calculator.py` → `__name__ == "__main__"`
- **Importing as module**: `import calculator` → `__name__ == "calculator"`

### The Solution

Use this pattern to prevent code from running during import:

**File: `calculator.py` (improved)**
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Only run this code if the file is executed directly
if __name__ == "__main__":
    print("Testing calculator...")
    print(add(5, 3))      # 8
    print(subtract(10, 4)) # 6
```

Now:
- **Import it**: Test code doesn't run
- **Run it directly**: Test code runs

### Visualizing `__name__`

```python
# File: demo.py
print(f"__name__ is: {__name__}")

def greet():
    print("Hello!")

if __name__ == "__main__":
    print("This file is being run directly")
    greet()
```

**Running directly:**
```bash
$ python demo.py
__name__ is: __main__
This file is being run directly
Hello!
```

**Importing it:**
```python
import demo
# Output: __name__ is: demo
# (The test code doesn't run)
```

## Common Use Cases

### 1. Testing Your Functions

```python
# File: math_utils.py
def factorial(n):
    """Calculate factorial of n."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test code that only runs when executed directly
if __name__ == "__main__":
    print("Testing math_utils...")
    print(f"factorial(5) = {factorial(5)}")     # 120
    print(f"fibonacci(7) = {fibonacci(7)}")     # 13
```

You can now:
- **Test it**: `python math_utils.py` runs your tests
- **Import it**: `from math_utils import factorial` doesn't run tests

### 2. Command-Line Scripts

Make your module usable both as a library and as a command-line tool:

```python
# File: converter.py
def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5/9

# Command-line interface
if __name__ == "__main__":
    print("Temperature Converter")
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_f = celsius_to_fahrenheit(temp_c)
    print(f"{temp_c}°C = {temp_f}°F")
```

Now you can:
- **Use as script**: `python converter.py` → interactive CLI
- **Import as module**: `from converter import celsius_to_fahrenheit` → use in code

### 3. Demonstrations and Examples

```python
# File: password_checker.py
def is_strong_password(password):
    """Check if password meets strength requirements."""
    if len(password) < 8:
        return False
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    return has_upper and has_lower and has_digit

# Demo that shows how the function works
if __name__ == "__main__":
    examples = ["weak", "StrongPass123", "NoDigits", "short1"]

    print("Password Strength Checker Demo:")
    for pwd in examples:
        is_strong = is_strong_password(pwd)
        status = "✓ Strong" if is_strong else "✗ Weak"
        print(f"  '{pwd}': {status}")
```

### 4. Running Tests

```python
# File: operations.py
def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

# Quick tests
if __name__ == "__main__":
    # Test multiply
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10

    # Test divide
    assert divide(10, 2) == 5
    assert divide(10, 0) is None

    print("All tests passed!")
```

## Best Practices for Creating Modules

### 1. Structure Your Module Properly

```python
# File: my_module.py

# 1. Imports at the top
import math
from datetime import date

# 2. Constants (if any)
PI = 3.14159
MAX_VALUE = 100

# 3. Function definitions
def function_one():
    """Docstring explaining what it does."""
    pass

def function_two():
    """Docstring explaining what it does."""
    pass

# 4. Main block at the bottom
if __name__ == "__main__":
    # Test code, demos, or CLI interface
    print("Testing my_module...")
    function_one()
    function_two()
```

### 2. Add Docstrings

```python
def circle_area(radius):
    """
    Calculate the area of a circle.

    Args:
        radius: The radius of the circle

    Returns:
        The area of the circle
    """
    import math
    return math.pi * radius ** 2
```

### 3. Keep Related Functions Together

```python
# Good: string_utils.py contains string-related functions
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    return sum(1 for c in s.lower() if c in 'aeiou')

def is_palindrome(s):
    return s == s[::-1]
```

### 4. Don't Put Important Logic in `__main__`

```python
# Bad: Important logic inside main block
if __name__ == "__main__":
    def critical_function():  # Don't define functions here!
        return 42

# Good: Define functions outside, call them inside
def critical_function():
    return 42

if __name__ == "__main__":
    result = critical_function()
    print(result)
```

## The Dual-Purpose Pattern

This pattern allows your file to work both ways:

| Use Case        | Command               | What Happens                                   |
|-----------------|-----------------------|------------------------------------------------|
| **As a module** | `import my_module`    | Functions are available, test code doesn't run |
| **As a script** | `python my_module.py` | Functions are defined AND test code runs       |

### Complete Example

```python
# File: stats_utils.py
import math

def mean(numbers):
    """Calculate the mean (average) of a list of numbers."""
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculate the median of a list of numbers."""
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    if n % 2 == 0:
        return (sorted_nums[n//2 - 1] + sorted_nums[n//2]) / 2
    return sorted_nums[n//2]

def std_dev(numbers):
    """Calculate the standard deviation of a list of numbers."""
    avg = mean(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)

# Test/demo code
if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print("Statistics Demo")
    print(f"Data: {data}")
    print(f"Mean: {mean(data)}")
    print(f"Median: {median(data)}")
    print(f"Std Dev: {std_dev(data):.2f}")
```

**Using it as a module:**
```python
from stats_utils import mean, median

scores = [85, 92, 78, 90, 88]
avg_score = mean(scores)
mid_score = median(scores)
```

**Using it as a script:**
```bash
$ python stats_utils.py
Statistics Demo
Data: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Mean: 5.0
Median: 5
Std Dev: 2.58
```

## Common Mistakes to Avoid

### 1. Circular Imports

```python
# File: a.py
import b
def func_a():
    return b.func_b()

# File: b.py
import a  # Circular import!
def func_b():
    return a.func_a()
```

**Solution**: Restructure your code to avoid circular dependencies.

### 2. Forgetting the `__main__` Guard

```python
# Bad: No main guard
def my_function():
    return 42

print("This will run on import!")  # Problem!
```

### 3. Module Name Conflicts

```python
# Don't name your file 'math.py' - it conflicts with built-in math!
import math  # This will import YOUR math.py, not Python's!
```

## Summary

- **Any Python file can be a module** - just write functions and import it
- **Use `if __name__ == "__main__"`** to prevent test code from running on import
- **Structure matters**: Imports → Functions → Main block
- **Write docstrings** for all your functions
- **Test your modules** by running them directly
- **Keep related functions together** in the same module
- **Avoid circular imports** and name conflicts

Creating modules is how you grow from writing single-file scripts to building organized, reusable code libraries. It's a fundamental skill for any Python programmer!
