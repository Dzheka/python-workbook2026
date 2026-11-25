# Vowels Used (Super Easy)

Which of the vowels `a e i o u` does a word use?

## Task

- Create a function `vowels_in(word)` that returns the vowels the word
  contains, each once, sorted alphabetically
- Create a function `missing_vowels(word)` that returns the vowels the word
  does **not** contain, sorted alphabetically

Upper- and lowercase count as the same letter; the answer is always lowercase.

## Examples

| Call                          | Returns                     |
|-------------------------------|-----------------------------|
| `vowels_in("banana")`         | `["a"]`                     |
| `vowels_in("Education")`      | `["a", "e", "i", "o", "u"]` |
| `missing_vowels("hello")`     | `["a", "i", "u"]`           |
| `missing_vowels("rhythm")`    | `["a", "e", "i", "o", "u"]` |

Hint: `VOWELS = set("aeiou")`, then `&` or `-` with `set(word.lower())`.
