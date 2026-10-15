# Functions in Python - Basics

## Introduction

Functions are reusable blocks of code that perform specific tasks. They are fundamental building blocks in Python programming that help you:

- **Avoid repetition**: Write code once, use it many times
- **Organize code**: Break complex problems into smaller, manageable pieces
- **Test easily**: Test individual functions independently
- **Improve readability**: Give meaningful names to operations
- **Maintain code**: Fix bugs in one place instead of many

Think of functions as mini-programs within your program. Just like you wouldn't want to rewrite the same paragraph in an essay multiple times, you don't want to repeat the same code throughout your program.

## Defining a Function

Use the `def` keyword to define a function:

```python
def greet():
    print("Hello, World!")
```

Components:
- `def` - keyword that starts a function definition
- `greet` - function name (follows variable naming rules)
- `()` - parentheses for parameters (empty here)
- `:` - colon to end the function header
- Indented block - the function body

## Calling a Function

To execute a function, use its name followed by parentheses:

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
greet()  # Output: Hello, World!
```

You can call a function as many times as needed.

## Parameters and Arguments

Functions become more powerful when they accept input values.

### Single Parameter

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet("Bob")    # Output: Hello, Bob!
```

- **Parameter**: Variable in the function definition (`name`)
- **Argument**: Actual value passed to the function (`"Alice"`, `"Bob"`)

### Multiple Parameters

```python
def area(length, width):
    a = length * width
    print(f"Area: {a}")

area(5, 3)   # Output: Area: 15
area(10, 4)  # Output: Area: 40
```

### Default Parameter Values

Parameters can have default values:

```python
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")              # Output: Hello, Alice!
greet("Bob", "Hi")          # Output: Hi, Bob!
greet("Charlie", "Hey")     # Output: Hey, Charlie!
```

Default parameters must come after non-default parameters.

## Return Values

Functions can return values using the `return` statement.

### Single Return Value

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# Use directly in expressions
total = add(10, 20) + add(5, 3)
print(total)  # Output: 38
```

### Return vs Print

**Important distinction:**

```python
# This function PRINTS but doesn't return
def add_and_print(a, b):
    print(a + b)

# This function RETURNS a value
def add_and_return(a, b):
    return a + b

# Comparison
result1 = add_and_print(3, 5)   # Prints: 8
print(result1)                  # Prints: None (no return value)

result2 = add_and_return(3, 5)  # No output
print(result2)                  # Prints: 8
```

**Key difference**:
- `print()` displays output to the user
- `return` provides a value that can be used in your code

### Functions Without Return

If a function doesn't have a `return` statement, it returns `None`:

```python
def greet(name):
    print(f"Hello, {name}!")

result = greet("Alice")  # Prints: Hello, Alice!
print(result)            # Prints: None
```

### Multiple Return Values

Functions can return multiple values as a tuple:

```python
import math

def calculate_circle(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

# Unpack the return values
area, circ = calculate_circle(5)
print(f"Area: {area:.2f}")              # Area: 78.54
print(f"Circumference: {circ:.2f}")     # Circumference: 31.42

# Or get as a tuple
result = calculate_circle(3)
print(result)  # (28.274..., 18.849...)
```

### Early Return

You can return early from a function:

```python
def is_even(number):
    if number % 2 == 0:
        return True
    return False

# More concise version
def is_even(number):
    return number % 2 == 0

print(is_even(4))  # True
print(is_even(7))  # False
```
