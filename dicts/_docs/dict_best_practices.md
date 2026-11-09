# Dictionary Best Practices

## Performance Characteristics

### Time Complexity

| Operation           | Average Case | Worst Case | Notes                                 |
|---------------------|--------------|------------|---------------------------------------|
| `d[key]` (get)      | O(1)         | O(n)       | Worst case rare (hash collisions)     |
| `d[key] = value`    | O(1)         | O(n)       | Set/update value                      |
| `del d[key]`        | O(1)         | O(n)       | Delete key-value pair                 |
| `key in d`          | O(1)         | O(n)       | Membership test                       |
| `d.get(key)`        | O(1)         | O(n)       | Safe access                           |
| `d.items()`         | O(1)         | O(1)       | Returns view (not copy)               |
| `len(d)`            | O(1)         | O(1)       | Number of key-value pairs             |
| Iteration           | O(n)         | O(n)       | Visit all items                       |

### Space Complexity

Dictionaries use O(n) space but have memory overhead compared to lists due to hash table implementation.

```python
import sys

# Memory comparison (approximate)
list_100 = list(range(100))
dict_100 = {i: i for i in range(100)}

sys.getsizeof(list_100)  # ~920 bytes
sys.getsizeof(dict_100)  # ~4704 bytes (more overhead)
```

## Common Patterns

### Pattern 1: Frequency Counting

```python
# Count occurrences of items
def count_frequencies(items):
    freq = {}
    for item in items:
        freq[item] = freq.get(item, 0) + 1
    return freq

count_frequencies("hello")  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Or use Counter
from collections import Counter
Counter("hello")  # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})
```

### Pattern 2: Grouping by Key

```python
# Group items by a property
def group_by(items, key_func):
    groups = {}
    for item in items:
        key = key_func(item)
        groups.setdefault(key, []).append(item)
    return groups

words = ["apple", "apricot", "banana", "blueberry"]
group_by(words, lambda w: w[0])
# {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}
```

### Pattern 3: Index Mapping

```python
# Map values to their indices
def create_index_map(items):
    return {item: i for i, item in enumerate(items)}

fruits = ["apple", "banana", "cherry"]
create_index_map(fruits)
# {'apple': 0, 'banana': 1, 'cherry': 2}
```

### Pattern 4: Caching/Memoization

```python
# Cache expensive function results
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

@memoize
def expensive_calculation(n):
    # Simulated expensive operation
    return n ** 2
```

## Common Mistakes to Avoid

### Mistake 1: Using Mutable Objects as Keys

```python
# DON'T: Lists are mutable and unhashable
try:
    d = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
except TypeError:
    pass

# DO: Use tuples instead
d = {(1, 2): "value"}  # OK - tuples are immutable
```

### Mistake 2: Not Using `get()` for Missing Keys

```python
# DON'T: Risky when key might not exist
d = {"a": 1}
# value = d["b"]  # KeyError!

# DO: Use get() with default
value = d.get("b", 0)  # Returns 0, no error
```

### Mistake 3: Modifying Dictionary During Iteration

```python
d = {"a": 1, "b": 2, "c": 3}

# DON'T: Modifies dict while iterating
# for key in d:
#     if d[key] == 2:
#         del d[key]  # RuntimeError: dictionary changed size during iteration

# DO: Iterate over a copy or collect keys to delete
for key in list(d.keys()):  # list() creates a copy
    if d[key] == 2:
        del d[key]
```

### Mistake 4: Forgetting Insertion Order (Pre-3.7)

```python
# Python 3.7+: Dictionaries maintain insertion order
d = {"b": 2, "a": 1, "c": 3}
list(d.keys())  # ['b', 'a', 'c'] - order preserved

# Before Python 3.7: Order was not guaranteed
# Use OrderedDict from collections if you need guaranteed order
```

### Mistake 5: Assuming `in` Checks Values

```python
d = {"name": "Alice", "age": 30}

"name" in d  # True (checks keys)
"Alice" in d  # False (doesn't check values!)

# To check if value exists:
"Alice" in d.values()  # True
```

## When NOT to Use Dictionaries

### 1. Sequential Access Needed

```python
# If you need ordered sequential access by position, use a list
items = [1, 2, 3, 4, 5]
items[0]  # First item
items[-1]  # Last item

# Dicts don't support positional indexing
d = {"a": 1, "b": 2}
# d[0]  # KeyError (0 is a key, not a position)
```

### 2. Multiple Values Per Key

```python
# DON'T: Overwrite values
d = {}
d["a"] = 1
d["a"] = 2  # Overwrites previous value

# DO: Use dict of lists
d = {"a": [1, 2]}  # Multiple values as a list
```

### 3. Need Ordering by Value

```python
# If you need items sorted by value, dict alone isn't enough
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Sort by value (returns list of tuples)
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
# [('Alice', 95), ('Charlie', 92), ('Bob', 87)]
```

### 4. Simple Attribute Access

```python
# For object-like attribute access, consider namedtuple or dataclass
from collections import namedtuple

# DON'T: Dict for simple structured data
person = {"name": "Alice", "age": 30}
name = person["name"]  # String lookup

# DO: Use namedtuple or dataclass
Person = namedtuple("Person", ["name", "age"])
person = Person("Alice", 30)
name = person.name  # Attribute access (faster, clearer)
```

## Quick Reference

### Creating Dictionaries

```python
{}                           # Empty dict
{"a": 1, "b": 2}             # Literal
dict(a=1, b=2)               # Constructor with kwargs
dict([("a", 1), ("b", 2)])   # Constructor with pairs
{x: x**2 for x in range(5)}  # Comprehension
```

### Accessing and Modifying

```python
d[key]                  # Get (raises KeyError if missing)
d.get(key, default)     # Get with default
d[key] = value          # Set/update
d.setdefault(key, val)  # Set only if missing
del d[key]              # Delete
d.pop(key, default)     # Remove and return
```

### Iterating

```python
for key in d: ...              # Iterate keys
for value in d.values(): ...   # Iterate values
for k, v in d.items(): ...     # Iterate pairs
```

### Checking and Combining

```python
key in d                # Membership test
len(d)                  # Number of items
d1.update(d2)           # Merge (mutates d1)
{**d1, **d2}            # Merge (new dict)
d1 | d2                 # Merge (Python 3.9+)
```

### Common Collections Helpers

```python
from collections import defaultdict, Counter

defaultdict(int)        # Dict with default values
Counter(items)          # Count items automatically
```

## Performance Tips

1. **Use `in` for membership tests** - It's O(1) for dicts vs O(n) for lists
2. **Use `get()` to avoid KeyError** - Cleaner than try/except for optional keys
3. **Use dict comprehensions** - More readable and often faster than loops
4. **Consider `defaultdict`** - Simpler code when you need default values
5. **Use `Counter`** - Purpose-built for counting, includes helpful methods
6. **Iterate over `.items()`** - More efficient than `for k in d: value = d[k]`
