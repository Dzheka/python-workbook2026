# Importing Modules in Python

## Introduction

Python's power comes not only from the language itself but also from its vast collection of pre-written code called **modules**. Modules are files containing Python functions, classes, and variables that you can use in your programs.

Think of modules as toolboxes:
- **Built-in modules**: Tools that come with Python (like `math`, `random`)
- **External modules**: Tools you can download (like `numpy`, `pandas`)
- **Your own modules**: Custom tools you create

Instead of writing everything from scratch, you can import and use code that others have already written and tested.

## Why Use Imports?

- **Save time**: Don't reinvent the wheel
- **Use tested code**: Modules are well-tested and reliable
- **Access advanced features**: Complex operations made simple
- **Organize code**: Split your program into multiple files

## Basic Import Syntax

### Importing an Entire Module

The simplest way to import a module:

```python
import math

# Use functions from the math module
result = math.sqrt(16)  # 4.0
area = math.pi * (5 ** 2)  # 78.53981633974483
```

When you `import math`, you must use the `math.` prefix to access its functions.

### Importing Specific Functions

Import only what you need:

```python
from math import sqrt, pi

# Use functions directly without the module prefix
result = sqrt(16)  # 4.0
area = pi * (5 ** 2)  # 78.53981633974483
```

This makes your code cleaner when you use the same functions many times.

### Importing Everything (Not Recommended)

```python
from math import *

# All math functions are now available
result = sqrt(16)
angle = sin(pi / 2)
```

**Warning**: This approach is generally discouraged because:
- It's unclear which functions come from which module
- Name conflicts can occur
- It makes code harder to read and maintain

### Using Aliases

Give modules shorter names:

```python
import math as m

result = m.sqrt(16)
area = m.pi * (5 ** 2)
```

This is especially useful for modules with long names.

## Common Built-in Modules

### `math` - Mathematical Functions

```python
import math

# Constants
print(math.pi)      # 3.141592653589793
print(math.e)       # 2.718281828459045

# Functions
print(math.sqrt(25))        # 5.0
print(math.pow(2, 3))       # 8.0
print(math.floor(4.7))      # 4
print(math.ceil(4.2))       # 5
print(math.sin(math.pi/2))  # 1.0
print(math.cos(0))          # 1.0
print(math.radians(180))    # 3.141592653589793
print(math.degrees(math.pi)) # 180.0
```

### `random` - Random Number Generation

```python
import random

# Random integer in range [1, 6]
dice = random.randint(1, 6)

# Random float in range [0.0, 1.0)
probability = random.random()

# Random choice from a list
color = random.choice(['red', 'green', 'blue'])

# Shuffle a list
cards = [1, 2, 3, 4, 5]
random.shuffle(cards)
```

### `datetime` - Date and Time

```python
from datetime import datetime, date, timedelta

# Current date and time
now = datetime.now()
print(now)  # 2024-03-15 14:30:00.123456

# Current date
today = date.today()
print(today)  # 2024-03-15

# Date arithmetic
tomorrow = today + timedelta(days=1)
next_week = today + timedelta(weeks=1)
```

## Where to Place Import Statements

**Best Practice**: Put all imports at the top of your file

```python
# Good: Imports at the top
import math
from datetime import date

def calculate_area(radius):
    return math.pi * radius ** 2

def is_weekend(day):
    return day.weekday() >= 5
```

```python
# Bad: Imports scattered throughout
def calculate_area(radius):
    import math  # Don't do this
    return math.pi * radius ** 2
```

## Common Patterns

### Pattern 1: Import Entire Module
**When to use**: Few function calls, or want to be explicit

```python
import math

def get_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
```

### Pattern 2: Import Specific Functions
**When to use**: Many calls to the same function

```python
from math import sqrt

def get_hypotenuse(a, b):
    return sqrt(a**2 + b**2)

def distance(x1, y1, x2, y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)
```

### Pattern 3: Import with Alias
**When to use**: Long module names, or industry conventions

```python
import numpy as np  # Common convention
import pandas as pd  # Common convention

# Much cleaner than typing numpy.array() repeatedly
data = np.array([1, 2, 3, 4, 5])
```

## Practice Tips

1. **Start simple**: Use `import module_name` when learning
2. **Read the documentation**: Use `help(math)` in Python to see what a module offers
3. **Check what's available**: Use `dir(math)` to list all functions in a module
4. **Consistent style**: Pick one import style and stick to it in a project

## Common Errors

### `ModuleNotFoundError`

```python
import nonexistent_module
# ModuleNotFoundError: No module named 'nonexistent_module'
```

**Solution**: Make sure the module is installed or spelled correctly.

### `ImportError`

```python
from math import nonexistent_function
# ImportError: cannot import name 'nonexistent_function'
```

**Solution**: Check the function name is spelled correctly and exists in the module.

### Name Conflicts

```python
from math import sqrt

def sqrt(x):  # Oops! Overwriting the imported function
    return x ** 0.5

print(sqrt(16))  # Which sqrt is called?
```

**Solution**: Avoid naming your functions the same as imported functions, or use module prefix (`math.sqrt`).

## Summary

- **Import modules** to access pre-written code
- **Use `import module`** for clarity and to avoid naming conflicts
- **Use `from module import function`** when you use specific functions frequently
- **Place imports at the top** of your file
- **Read module documentation** to discover available functions
- **Practice with built-in modules** like `math`, `random`, and `datetime`

Remember: Importing modules is like using a library - you don't need to write every book yourself, just know which shelf to find the one you need!

## Next Steps

Once you're comfortable importing and using built-in modules, you can learn how to create your own modules and make your code reusable. See [`modules.md`](modules.md) to learn about:
- Creating your own importable modules
- The `if __name__ == "__main__"` pattern
- Best practices for module organization
