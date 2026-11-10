# Isogram

Check whether a word or phrase has no repeating letters.

## Task

Write a function `is_isogram(text)` that returns `True` if no letter appears more than once, and `False` otherwise.

- The check is case-insensitive (`A` and `a` count as the same letter)
- Spaces and hyphens are ignored
- An empty string is an isogram

## Template

```python
def is_isogram(text: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_isogram("lumberjacks"))  # True
    print(is_isogram("isograms"))  # False
    print(is_isogram("Alphabet"))  # False
    print(is_isogram("thumbscrew-japingly"))  # True
    print(is_isogram("Emily Jung Schwartzkopf"))  # True
    print(is_isogram(""))  # True
```
