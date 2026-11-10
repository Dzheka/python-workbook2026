# Isomorphic Strings

Check if two strings are isomorphic.

## Task

Write a function `isomorphic_strings(s, t)` that determines if two strings are isomorphic.

- Two strings are isomorphic if the characters in `s` can be replaced to get `t`
- Each character must map to exactly one character; different characters cannot map to the same character
- A character may map to itself

## Template

```python
def isomorphic_strings(s: str, t: str) -> bool:
    pass


if __name__ == "__main__":
    print(isomorphic_strings("egg", "add"))  # True
    print(isomorphic_strings("foo", "bar"))  # False
    print(isomorphic_strings("paper", "title"))  # True
    print(isomorphic_strings("ab", "abc"))  # False
    print(isomorphic_strings("abc", "abc"))  # True
    print(isomorphic_strings("", ""))  # True
```
