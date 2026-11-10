# Set Best Practices

## Performance: Why Sets Are Fast

Sets use **hash tables** internally, which provides O(1) average-case time complexity for common operations:

| Operation               | Set  | List          |
|-------------------------|------|---------------|
| Check membership (`in`) | O(1) | O(n)          |
| Add element             | O(1) | O(1) or O(n)* |
| Remove element          | O(1) | O(n)          |
| Get length              | O(1) | O(1)          |

*List append is amortized O(1), but insert at arbitrary position is O(n).

**Amortized** means averaged over many calls: both lists and sets occasionally resize their underlying storage (an O(n)
event), but it happens rarely enough that the average cost per `append`/`add` stays O(1).

## Common Patterns

### Pattern 1: Remove Duplicates from a List

```python
# Preserves NO order
unique = list(set(my_list))

# Preserves order (Python 3.7+)
unique = list(dict.fromkeys(my_list))
```

### Pattern 2: Filter with Set Lookup

```python
allowed = {"admin", "editor", "viewer"}
users = [("alice", "admin"), ("bob", "guest"), ("carol", "editor")]

# Fast lookup using set
authorized = [(name, role) for name, role in users if role in allowed]
```

## Common Mistakes

### Mistake 1: Creating Empty Set with `{}`

```python
# WRONG - creates empty dict
empty = {}
type(empty)  # <class 'dict'>

# CORRECT - use set()
empty = set()
type(empty)  # <class 'set'>
```

### Mistake 2: Trying to Add Mutable Elements

```python
s = set()

# WRONG - lists are mutable
s.add([1, 2, 3])  # TypeError: unhashable type: 'list'

# CORRECT - use tuple instead
s.add((1, 2, 3))  # Works!
```

### Mistake 3: Assuming Order

```python
s = {3, 1, 2}
# Don't assume iteration order!
# Sets are unordered collections
```

### Mistake 4: Modifying Set While Iterating

```python
s = {1, 2, 3, 4, 5}

# WRONG - RuntimeError
for item in s:
    if item % 2 == 0:
        s.remove(item)

# CORRECT - iterate over a copy
for item in s.copy():
    if item % 2 == 0:
        s.remove(item)

# BETTER - use set comprehension
s = {item for item in s if item % 2 != 0}
```

## When NOT to Use Sets

- When you need to maintain order (use `list` or `dict`)
- When you need duplicate elements (use `list`)
- When you need to access elements by index (use `list`)
- When elements are unhashable (mutable types like lists, dicts)

## Quick Reference

```python
# Creation
s = set()                    # empty set
s = {1, 2, 3}               # literal
s = set([1, 2, 2, 3])       # from iterable

# Modification
s.add(x)                     # add element
s.remove(x)                  # remove (raises KeyError if missing)
s.discard(x)                 # remove (no error if missing)
s.pop()                      # remove and return arbitrary element
s.clear()                    # remove all

# Operations
s | t                        # union
s & t                        # intersection
s - t                        # difference
s ^ t                        # symmetric difference

# Tests
x in s                       # membership
s <= t                       # subset
s >= t                       # superset
s.isdisjoint(t)             # no common elements
```
