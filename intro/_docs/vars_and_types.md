# Variables and Data Types - Essential Concepts

This guide covers all the fundamental concepts you need to solve exercises.

## Variables

Variables are containers that store data values. In Python, you create a variable by assigning a value to it.

```python
# Creating variables
name = "Alice"
age = 25
price = 12.99
```

**Rules for variable names:**

- Must start with a letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive (`age` and `Age` are different)
- Cannot use Python keywords (`if`, `for`, `while`, `def`, etc.)
- Avoid reusing built-in function names (`print`, `input`, `sum`, etc.) — Python allows it, but the function stops working afterward

## Data Types

| Data Type | Name    | Description                          | Examples                          |
|-----------|---------|--------------------------------------|-----------------------------------|
| `str`     | String  | Text data enclosed in quotes         | `"Hello"`, `'John'`, `"123"`      |
| `int`     | Integer | Whole numbers without decimal points | `25`, `0`, `2024`, `-5`           |
| `float`   | Float   | Numbers with decimal points          | `19.99`, `25.5`, `3.14159`, `0.0` |

### Examples in code

```python
# String examples
message = "Hello, World!"
name = 'John'
text_number = "123"  # This is text, not a number

# Integer examples
age = 25
count = 0
year = 2024

# Float examples
price = 19.99
temperature = 25.5
pi = 3.14159
```

## Input and Output

### Getting input from users

```python
name = input("Enter your name: ")  # Always returns a string
age_str = input("Enter your age: ")  # This is a string, not a number
```

The prompt text is **optional**, and its wording is up to you. Writing
`input()` with no prompt works exactly the same: the exercise checker never
sees your prompts, only the values you read and what you print. So all of
these are accepted:

```python
name = input("Enter your name: ")  # with a prompt
name = input("Your name? ")        # any wording — also fine
name = input()                     # no prompt — also fine
```

### Displaying output

```python
print("Hello, World!")              # Simple text
print("Your age is:", age)          # Multiple items
print(f"Hello {name}")              # f-string formatting
```

## Type Conversion

Since `input()` always returns a string, you often need to convert it to numbers.

```python
# Converting strings to numbers
age_str = input("Enter age: ")
age = int(age_str)                  # Convert to integer

price_str = input("Enter price: ")
price = float(price_str)            # Convert to float

# You can do it in one line
age = int(input("Enter age: "))
price = float(input("Enter price: "))
```

## Arithmetic Operations

For detailed arithmetic operators and examples, see [`math_operators.md`](math_operators.md).

## String Formatting and Operations

For detailed string formatting patterns and examples, see [`string_formatting.md`](string_formatting.md).

### Basic string operations

```python
# Simple concatenation
first_name = "John"
last_name = "Doe"
full_name = first_name + " " + last_name

# Using print() with multiple values
name = "Alice"
age = 25
print("Hello", name, "you are", age, "years old")
```

### f-strings (RECOMMENDED)

```python
name = "Alice"
age = 25
print(f"Hello {name}, you are {age} years old")
print(f"The area is: {area:.2f}")  # 2 decimal places
```

### String methods (useful to know)

```python
text = "Hello World"
print(text.upper())         # HELLO WORLD
print(text.lower())         # hello world
print(len(text))            # 11
```

## Comments

Use comments to explain your code:

```python
# This is a single-line comment
name = input("Enter your name: ")  # Get user's name
```

## Program Structure

A typical program follows this pattern:

```python
# 1. Get input from user
radius = float(input("Enter radius: "))

# 2. Perform calculations
pi = 3.14159
area = pi * radius ** 2

# 3. Display results
print(f"The area is: {area}")
```

## Common Patterns for Exercises

### Pattern 1: Simple calculation

```python
# Get two numbers and calculate their sum
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum is: {sum_result}")
```

### Pattern 2: Formula application

```python
# Calculate rectangle area
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print(f"The area is: {area}")
```

### Pattern 3: Unit conversion

```python
# Convert seconds to minutes and seconds
total_seconds = int(input("Enter seconds: "))
minutes = total_seconds // 60
seconds = total_seconds % 60
print(f"{total_seconds} seconds = {minutes} minutes and {seconds} seconds")
```

## Tips for Success

1. **Always convert input to the right type:**
   ```python
   # Wrong: age = input("Enter age: ")  # This is a string!
   # Right: age = int(input("Enter age: "))
   ```

2. **Use descriptive variable names:**
   ```python
   # Wrong: x = 5, y = 3, z = x * y
   # Right: length = 5, width = 3, area = length * width
   ```

3. **Pay attention to output formatting:**
   ```python
   # If exercise asks for "The result is: 42"
   print(f"The result is: {result}")  # Exact format matters
   ```

4. **Test with the example data:**
    - Run your program with the exact input from the exercise
    - Check that the output matches exactly

5. **Common mistakes to avoid:**
    - Forgetting to convert strings to numbers
    - Using wrong data types (int vs float)
    - Incorrect output formatting
    - Wrong arithmetic operations

## Quick Reference

| Operation         | Example                           | Result  |
|-------------------|-----------------------------------|---------|
| Get string input  | `name = input("Name: ")`          | String  |
| Get integer input | `age = int(input("Age: "))`       | Integer |
| Get float input   | `price = float(input("Price: "))` | Float   |
| Addition          | `5 + 3`                           | 8       |
| Subtraction       | `5 - 3`                           | 2       |
| Multiplication    | `5 * 3`                           | 15      |
| Division          | `5 / 3`                           | 1.666...|
| Integer division  | `5 // 3`                          | 1       |
| Remainder         | `5 % 3`                           | 2       |
| Power             | `5 ** 3`                          | 125     |
| Print simple      | `print("Hello")`                  | Hello   |
| Print variable    | `print(f"Age: {age}")`            | Age: 25 |
