# Vowel Count (Easy)

Count the vowels and consonants in a piece of English text.

The vowels are `a`, `e`, `i`, `o`, `u`, in either case. A consonant is any
other Latin letter. Spaces, digits and punctuation are neither.

## Task

- Create a function `count_vowels(text)` that returns the number of vowels
- Create a function `count_consonants(text)` that returns the number of
  consonants
- Create a function `more_vowels(text)` that returns `True` if the text has
  more vowels than consonants

## Examples

| Call                                  | Returns |
|---------------------------------------|---------|
| `count_vowels("hello")`               | `2`     |
| `count_vowels("AEIOU")`               | `5`     |
| `count_consonants("hello")`           | `3`     |
| `count_consonants("Python Is Fun!")`  | `8`     |
| `count_consonants("a1 b2")`           | `1`     |
| `more_vowels("audio")`                | `True`  |
| `more_vowels("hello")`                | `False` |

Hint: `text.lower()` saves you from checking both cases, and
`"a" <= ch <= "z"` tells whether `ch` is a letter.
