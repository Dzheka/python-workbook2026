# Shared Letters (Medium)

Look at the letters several words are made of.

## Task

- Create a function `common_letters(words)` that returns the letters that
  appear in **every** word, sorted alphabetically
- Create a function `any_letters(words)` that returns the letters that appear
  in **at least one** word, sorted alphabetically

Only letters count (skip spaces, digits, punctuation). Upper- and lowercase
are the same letter; the answer is lowercase. An empty list of words gives
`[]` for both functions.

## Examples

| Call                                          | Returns                          |
|-----------------------------------------------|----------------------------------|
| `common_letters(["apple", "grape", "pear"])`  | `["a", "e", "p"]`                |
| `common_letters(["cat", "dog"])`              | `[]`                             |
| `any_letters(["Hi!", "ho"])`                  | `["h", "i", "o"]`                |
| `any_letters([])`                             | `[]`                             |

Hint: start with the letters of the first word and keep only what each next
word also has (`&=`). For the second function start from `set()` and use `|=`.
