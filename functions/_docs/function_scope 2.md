# Functions in Python - Scope

Variables created inside a function are **local** to that function.

## Local Variables

```python
def calculate():
    x = 10  # Local variable
    return x * 2

result = calculate()
print(result)  # 20
# print(x)  # Error: x is not defined
```

## Global Variables

Variables defined outside functions are global:

```python
total = 0  # Global variable

def add_to_total(value):
    global total
    total += value

add_to_total(5)
add_to_total(3)
print(total)  # 8
```

**Best Practice**: Avoid using `global`. Instead, pass values as parameters and return results.

## Parameters Create Local Variables

```python
def greet(name):  # name is a local variable
    message = f"Hello, {name}!"  # the message is also local
    return message

print(greet("Alice"))
# print(name)  # Error: name is not defined
```

## Shadowing Global Variables

Local variables can have the same name as global variables:

```python
x = 100  # Global

def calculate():
    x = 10  # Local (different from global x)
    return x * 2

print(calculate())  # 20
print(x)            # 100 (global unchanged)
```
