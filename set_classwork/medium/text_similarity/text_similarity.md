# Text Similarity (Medium)

How alike are two texts? One simple measure looks only at **which words** they
use:

```
similarity = (words in both texts) / (words in at least one text)
```

`1.0` means the same set of words, `0.0` means no word in common.

## Task

- Create a function `similarity(text1, text2)` that returns this number,
  rounded to 2 decimal places. If both texts have no words at all, return
  `1.0`
- Create a function `unique_to_first(text1, text2)` that returns the words of
  `text1` that `text2` does not use, sorted alphabetically

Words are separated by spaces. Upper- and lowercase count as the same word;
the answer is lowercase. There is no punctuation.

## Examples

| Call                                                    | Returns           |
|---------------------------------------------------------|-------------------|
| `similarity("the cat sat", "the cat ran")`              | `0.5`             |
| `similarity("I like tea", "tea I like")`                | `1.0`             |
| `similarity("red", "blue")`                             | `0.0`             |
| `unique_to_first("the cat sat", "The dog SAT")`         | `["cat"]`         |

In the first example the words in both are `the, cat` (2), the words in at
least one are `the, cat, sat, ran` (4), so `2 / 4 = 0.5`.

Hint: `set(text.lower().split())`.
