# Phrase Anagram Checker

Check if two phrases are anagrams of each other, ignoring spaces and case.

## Task

Write a function `is_phrase_anagram(phrase1, phrase2)` that determines if two phrases are anagrams.

- Two phrases are anagrams if they contain the same letters with the same frequencies, ignoring spaces and case

## Template

```python
def is_phrase_anagram(phrase1: str, phrase2: str) -> bool:
    pass


if __name__ == "__main__":
    print(is_phrase_anagram("listen", "silent"))  # True
    print(is_phrase_anagram("conversation", "voices rant on"))  # True
    print(is_phrase_anagram("The Eyes", "They See"))  # True
    print(is_phrase_anagram("hello world", "world peace"))  # False
    print(is_phrase_anagram("abc", "a b c"))  # True
    print(is_phrase_anagram("", ""))  # True
```
