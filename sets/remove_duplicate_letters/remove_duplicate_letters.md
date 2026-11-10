# Remove Duplicate Letters

Remove duplicate characters from a string while preserving order.

## Task

Write a function `remove_duplicate_letters(text)` that returns a new string with duplicate characters removed.

- Preserve the order of first occurrence of each character
- The comparison should be case-sensitive ('A' and 'a' are different)

## Template

```python
def remove_duplicate_letters(text: str) -> str:
    pass


if __name__ == "__main__":
    print(remove_duplicate_letters("hello"))  # "helo"
    print(remove_duplicate_letters("mississippi"))  # "misp"
    print(remove_duplicate_letters("abcabc"))  # "abc"
    print(remove_duplicate_letters("AaAaBb"))  # "AaBb"
    print(remove_duplicate_letters(""))  # ""
```
