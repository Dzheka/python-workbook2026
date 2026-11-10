# Character Count

Count the frequency of each character in a string.

## Task

Write a function `chars_count(text)` that takes a string and returns a dictionary mapping each character to the number
of times it occurs.

- Count every character, including spaces, punctuation, and digits
- Counting is case-sensitive

## Template

```python
def chars_count(text: str) -> dict[str, int]:
    pass


if __name__ == "__main__":
    print(chars_count("hello"))  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    print(chars_count(""))  # {}
    print(chars_count("aaa"))  # {'a': 3}
    print(chars_count("hello world"))  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
    print(chars_count("AaBbCc"))  # {'A': 1, 'a': 1, 'B': 1, 'b': 1, 'C': 1, 'c': 1}
    print(chars_count("12321"))  # {'1': 2, '2': 2, '3': 1}
```
