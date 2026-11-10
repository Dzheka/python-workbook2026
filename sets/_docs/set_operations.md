# Set Operations

Python sets support all standard mathematical set operations. These operations are powerful tools for comparing and
combining collections.

## Visual Overview

```
A = {2, 3, 5}
B = {3, 5, 7}

Union (A | B):          {2, 3, 5, 7}  - all elements from both
Intersection (A & B):   {3, 5}        - elements in both
Difference (A - B):     {2}           - elements in A but not B
Symmetric Diff (A ^ B): {2, 7}        - elements in either, but not both
```

## Union

Elements that are in **either** set (or both).

```python
a = {2, 3, 5}
b = {3, 5, 7}

# Method 1: operator
a | b                # {2, 3, 5, 7}

# Method 2: method (can take any iterable)
a.union(b)           # {2, 3, 5, 7}
a.union([3, 5, 7])   # {2, 3, 5, 7}

# Multiple sets
a | b | {11, 13}     # {2, 3, 5, 7, 11, 13}
```

## Intersection

Elements that are in **both** sets.

```python
a = {2, 3, 5}
b = {3, 5, 7}

# Method 1: operator
a & b                # {3, 5}

# Method 2: method
a.intersection(b)    # {3, 5}

# Multiple sets
a & b & {3, 11}      # {3}
```

## Difference

Elements in the **first** set but **not** in the second.

```python
a = {2, 3, 5}
b = {3, 5, 7}

# Method 1: operator
a - b                # {2}
b - a                # {7}

# Method 2: method
a.difference(b)      # {2}
```

## Symmetric Difference

Elements in **either** set, but **not in both** (XOR operation).

```python
a = {2, 3, 5}
b = {3, 5, 7}

# Method 1: operator
a ^ b                      # {2, 7}

# Method 2: method
a.symmetric_difference(b)  # {2, 7}
```

## Subset and Superset

```python
a = {2, 3}
b = {2, 3, 5, 7}

# Subset: is every element of a in b?
a <= b               # True (a is subset of b)
a.issubset(b)        # True

a < b                # True (a is proper subset - not equal)

# Superset: does b contain all elements of a?
b >= a               # True (b is superset of a)
b.issuperset(a)      # True
```

## Disjoint Sets

Two sets are **disjoint** if they have no elements in common.

```python
a = {2, 3, 5}
b = {7, 11, 13}
c = {5, 7, 11}

a.isdisjoint(b)      # True - no common elements
a.isdisjoint(c)      # False - both have 5
```

## In-Place Operations

Modify the set directly instead of creating a new one:

```python
a = {2, 3, 5}

a |= {7, 11}         # a.update({7, 11})
a &= {3, 5, 7}       # a.intersection_update({3, 5, 7})
a -= {5}             # a.difference_update({5})
a ^= {2, 11}         # a.symmetric_difference_update({2, 11})
```

## Summary Table

| Operation      | Operator | Method                      | Description                  |
|----------------|----------|-----------------------------|------------------------------|
| Union          | `a \| b` | `a.union(b)`                | All elements from both sets  |
| Intersection   | `a & b`  | `a.intersection(b)`         | Elements in both sets        |
| Difference     | `a - b`  | `a.difference(b)`           | Elements in a but not b      |
| Symmetric Diff | `a ^ b`  | `a.symmetric_difference(b)` | Elements in either, not both |
| Subset         | `a <= b` | `a.issubset(b)`             | Is a contained in b?         |
| Superset       | `a >= b` | `a.issuperset(b)`           | Does a contain b?            |
| Disjoint       | -        | `a.isdisjoint(b)`           | No common elements?          |
