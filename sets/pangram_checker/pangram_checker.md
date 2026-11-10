# Pangram Checker

Check if a string contains every letter of the alphabet.

## Task

Write a function `is_pangram(text)` that returns `True` if the input string contains every letter of the English
alphabet at least once, and `False` otherwise.

- The check should be case-insensitive
- Non-letter characters (spaces, punctuation, numbers) should be ignored

## Template

```python
def is_pangram(text: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_pangram("The quick brown fox jumps over the lazy dog"))  # True
    print(is_pangram("Pack my box with five dozen liquor jugs"))  # True
    print(is_pangram("Hello World"))  # False
    print(is_pangram("abcdefghijklmnopqrstuvwxyz"))  # True
    print(is_pangram("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # True
```
