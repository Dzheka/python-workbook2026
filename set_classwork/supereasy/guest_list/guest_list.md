# Guest List (Super Easy)

The party's guest list is a **set** of names. These functions change that set
directly; they do not make a new one.

## Task

- Create a function `add_guest(guests, name)` that adds `name` to the set.
  It returns `True` if the name was new and `False` if it was already there
- Create a function `remove_guest(guests, name)` that removes `name` from the
  set. It returns `True` if the name was there and `False` if it was not. A
  missing name must **not** cause an error

## Examples

```python
>>> guests = {"Ali", "Sara"}
>>> add_guest(guests, "Bek")
True
>>> add_guest(guests, "Ali")
False
>>> remove_guest(guests, "Sara")
True
>>> remove_guest(guests, "Timur")
False
>>> sorted(guests)
['Ali', 'Bek']
```

Hint: check `name in guests` first. `discard` removes without an error,
`remove` raises one.
