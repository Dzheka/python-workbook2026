# Longest Substring Without Repeating Characters

Find the length of the longest substring without repeating characters.

## Task

Write a function `longest_substring_without_repeating(s)` that returns the length of the longest substring that contains no repeating characters.

- A substring is a contiguous sequence of characters
- Case-sensitive: 'A' and 'a' are different characters
- Every character counts: letters, digits, spaces, and punctuation

## Template

```python
def longest_substring_without_repeating(s: str) -> int:
    pass


if __name__ == "__main__":
    print(longest_substring_without_repeating("abcabcbb"))  # 3 ("abc")
    print(longest_substring_without_repeating("bbbbb"))  # 1 ("b")
    print(longest_substring_without_repeating("pwwkew"))  # 3 ("wke")
    print(longest_substring_without_repeating(""))  # 0
    print(longest_substring_without_repeating("a"))  # 1
    print(longest_substring_without_repeating("abcdef"))  # 6
    print(longest_substring_without_repeating("dvdf"))  # 3 ("vdf")
```
