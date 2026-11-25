# Spell Checker (Hard)

A spell checker knows a list of correct words. It finds the words of a text
that it does not know, and suggests corrections for a typo.

A correction is a known word that is **one edit** away from the typo. One edit
is one of:

- **delete** one letter: `"helo"` → `"hel"`, `"heo"`, ...
- **insert** one letter anywhere: `"helo"` → `"hello"`, `"ahelo"`, ...
- **replace** one letter: `"helo"` → `"halo"`, `"help"`, ...

## Task

- Create a function `unknown_words(text, dictionary)` that returns the words
  of `text` that are not in `dictionary`, lowercase, each once, in the order
  they first appear. Words are separated by spaces; remove the characters
  `. , ! ?` from both ends of a word before checking
- Create a function `suggest(word, dictionary)` that returns the known words
  one edit away from `word` (lowercase letters `a`–`z`), sorted
  alphabetically. The word itself is not a suggestion

## Examples

```python
dictionary = ["hello", "help", "halo", "held", "world", "word", "a", "the"]
```

| Call                                                     | Returns                              |
|----------------------------------------------------------|--------------------------------------|
| `unknown_words("Helo wrld, the helo!", dictionary)`      | `["helo", "wrld"]`                   |
| `suggest("helo", dictionary)`                            | `["halo", "held", "hello", "help"]`  |
| `suggest("wrld", dictionary)`                            | `["world"]`                          |
| `suggest("xyz", dictionary)`                             | `[]`                                 |

Hint: `known = set(dictionary)` makes every check instant. For `suggest`, build
a set of **all** one-edit variants with a loop over the split points
`word[:i]`, `word[i:]` and a loop over the 26 letters, then `& known`. A
four-letter word has about 230 variants — that's fine.
