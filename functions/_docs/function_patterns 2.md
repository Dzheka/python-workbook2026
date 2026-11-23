# Functions in Python - Common Patterns

The following are common kinds of functions you'll write repeatedly.

## Mathematical Calculations

```python
import math

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle."""
    return math.pi * radius ** 2

def calculate_hypotenuse(a: float, b: float) -> float:
    """Calculate hypotenuse using Pythagorean theorem."""
    return math.sqrt(a ** 2 + b ** 2)

print(calculate_circle_area(5))     # 78.54...
print(calculate_hypotenuse(3, 4))   # 5.0
```

## Boolean-Returning Functions

Functions that return `True` or `False` often start with "is" or "has":

```python
def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0

def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_palindrome(text: str) -> bool:
    """Check if the text is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

print(is_even(4))              # True
print(is_prime(17))            # True
print(is_palindrome("radar"))  # True
```

## Conversion Functions

```python
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

def binary_to_decimal(binary: str) -> int:
    """Convert binary string to decimal integer."""
    return int(binary, 2)

print(fahrenheit_to_celsius(98.6))    # 37.0
print(celsius_to_fahrenheit(100))     # 212.0
print(binary_to_decimal("1010"))      # 10
```

## String Manipulation

```python
def caesar_cipher(text: str, shift: int) -> str:
    """Encrypt text using Caesar cipher."""
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26
            result += chr(start + shifted)
        else:
            result += char
    return result

def count_vowels(text: str) -> int:
    """Count vowels in text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)

print(caesar_cipher("HELLO", 3))   # KHOOR
print(count_vowels("Hello World"))  # 3
```

## Accumulation Pattern

```python
def sum_of_digits(number: int) -> int:
    """Calculate the sum of digits in a number."""
    total = 0
    number = abs(number)  # Handle negative numbers
    while number > 0:
        total += number % 10
        number //= 10
    return total

def factorial(n: int) -> int:
    """Calculate factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(sum_of_digits(12345))  # 15
print(factorial(5))          # 120
```

## Validation Pattern

```python
def is_triangle(a: float, b: float, c: float) -> bool:
    """Check if three sides can form a triangle."""
    return (a + b > c) and (a + c > b) and (b + c > a)

def is_leap_year(year: int) -> bool:
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

print(is_triangle(3, 4, 5))   # True
print(is_triangle(1, 1, 10))  # False
print(is_leap_year(2024))     # True
print(is_leap_year(2023))     # False
```
