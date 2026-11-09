# Anagram Checker

Check if two words are anagrams of each other.

## Task

Write a function `is_anagram(word1, word2)` that determines if two words are anagrams.

- Two words are anagrams if they contain the same characters with the same frequencies
- The comparison is case-sensitive ('A' and 'a' are different)

## Template

```python
def is_anagram(word1: str, word2: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_anagram("listen", "silent"))  # True
    print(is_anagram("hello", "world"))  # False
    print(is_anagram("abc", "abcd"))  # False
    print(is_anagram("test", "test"))  # True
    print(is_anagram("", ""))  # True
    print(is_anagram("a", "a"))  # True
```
