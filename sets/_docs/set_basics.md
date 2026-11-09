# Set Basics

A **set** is an unordered collection of unique elements. Sets are one of Python's built-in data types and are extremely
useful when you need to:

- Remove duplicates from a collection
- Check membership quickly (O(1) average time)
- Perform mathematical set operations (union, intersection, etc.)

## Creating Sets

```python
# Empty set (note: {} creates an empty dict, not a set!)
empty_set = set()

# Set from literal
fruits = {"apple", "banana", "cherry"}

# Set from list (removes duplicates)
numbers = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}

# Set from string (each character becomes an element)
chars = set("hello")  # {'h', 'e', 'l', 'o'}
```

## Key Characteristics

| Feature           | Description                                                  |
|-------------------|--------------------------------------------------------------|
| Unordered         | Elements have no index; order is not guaranteed              |
| Unique            | No duplicate elements allowed                                |
| Mutable           | Can add/remove elements (but elements must be immutable)     |
| Hashable elements | Only immutable types can be set elements (no lists or dicts) |

## Basic Operations

### Adding Elements

```python
s = {1, 2, 3}
s.add(4)        # {1, 2, 3, 4}
s.add(2)        # {1, 2, 3, 4} - no change, 2 already exists
```

### Removing Elements

```python
s = {1, 2, 3, 4}

s.remove(3)     # {1, 2, 4} - raises KeyError if not found
s.discard(10)   # {1, 2, 4} - no error if not found
s.pop()         # removes and returns an arbitrary element
s.clear()       # set() - removes all elements
```

### Membership Testing

```python
s = {"apple", "banana", "cherry"}

"apple" in s      # True
"mango" in s      # False
"mango" not in s  # True
```

## When to Use Sets

| Use Case                | Why Sets?                                       |
|-------------------------|-------------------------------------------------|
| Remove duplicates       | `list(set(my_list))` is the fastest way         |
| Fast membership checks  | O(1) vs O(n) for lists                          |
| Mathematical operations | Union, intersection, difference built-in        |
| Tracking seen items     | Perfect for "have I seen this before?" patterns |

## Set vs List: Performance Comparison

```python
# Checking if item exists:
my_list = [1, 2, 3, ..., 1000000]
my_set = {1, 2, 3, ..., 1000000}

999999 in my_list  # O(n) - slow, checks each element
999999 in my_set   # O(1) - fast, uses hash lookup
```

## Frozen Sets

If you need an immutable set (e.g., to use as a dictionary key), use `frozenset`:

```python
fs = frozenset([1, 2, 3])
# fs.add(4)  # Error! frozenset is immutable

# Can be used as dict key
d = {fs: "value"}
```
