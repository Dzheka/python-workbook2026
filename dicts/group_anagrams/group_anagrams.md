# Group Anagrams

Group words that are anagrams of each other.

## Task

Write a function `group_anagrams(words)` that groups words that are anagrams of each other.

- Return a list of lists, where each inner list contains words that are anagrams of each other
- Neither the order of the groups nor the order of words within a group matters
- The comparison is case-sensitive

## Template

```python
def group_anagrams(words: list[str]) -> list[list[str]]:
    pass


if __name__ == "__main__":
    print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

    print(group_anagrams(["abc", "def"]))
    # [['abc'], ['def']]

    print(group_anagrams(["abc", "bca", "cab"]))
    # [['abc', 'bca', 'cab']]

    print(group_anagrams([]))
    # []

    print(group_anagrams(["hello"]))
    # [['hello']]
```
