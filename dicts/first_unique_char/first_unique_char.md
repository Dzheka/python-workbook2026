# First Unique Character

Find the first character that appears only once in a string.

## Task

Write a function `first_unique_char(text)` that returns the first character in the string that appears exactly once.

- Return `None` if no character appears exactly once
- The check is case-sensitive
- Consider every character, including spaces and punctuation

## Template

```python
def first_unique_char(text: str) -> str | None:
    pass


if __name__ == "__main__":
    print(first_unique_char("leetcode"))  # 'l'
    print(first_unique_char("loveleetcode"))  # 'v'
    print(first_unique_char("aabbcc"))  # None
    print(first_unique_char("abcab"))  # 'c'
    print(first_unique_char("a"))  # 'a'
    print(first_unique_char(""))  # None
```
