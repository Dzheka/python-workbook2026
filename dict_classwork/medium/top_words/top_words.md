# Top Words (Medium)

Which words does a text use the most?

## Task

- Create a function `top_words(text, k)` that returns the `k` most frequent
  words as a list of `(word, count)` tuples, most frequent first. Words with
  the same count go alphabetically

Rules:

- `"The"` and `"the"` are the same word: work in lowercase
- the marks `.` `,` `!` `?` around a word are not part of it: `"dog."` is
  `"dog"`
- if the text has fewer than `k` different words, return all of them

## Examples

```python
text = "The dog saw the cat. The cat ran! A dog?"
```

| Call                   | Returns                                        |
|------------------------|------------------------------------------------|
| `top_words(text, 3)`   | `[("the", 3), ("cat", 2), ("dog", 2)]`         |
| `top_words(text, 1)`   | `[("the", 3)]`                                 |
| `top_words("", 2)`     | `[]`                                           |

Hint: count into a dictionary, then
`sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))` sorts by count
going down and by word going up. `word.strip(".,!?")` cleans a word.
