# Word Count (Super Easy)

Count how many times each word appears in a text.

## Task

- Create a function `count_words(text)` that returns a dictionary: word → how
  many times it appears. Words are separated by spaces; `"The"` and `"the"`
  are the same word, so use lowercase keys
- Create a function `unique_words(text)` that returns the words that appear
  **exactly once**, sorted alphabetically

## Examples

| Call                                     | Returns                          |
|------------------------------------------|----------------------------------|
| `count_words("the cat and the dog")`     | `{"the": 2, "cat": 1, "and": 1, "dog": 1}` |
| `count_words("Go go GO")`                | `{"go": 3}`                      |
| `count_words("")`                        | `{}`                             |
| `unique_words("the cat and the dog")`    | `["and", "cat", "dog"]`          |

Hint: `counts[word] = counts.get(word, 0) + 1`. Then loop over
`counts.items()`.
