# Title Case (Medium)

Make every word start with a capital letter — by hand, letter by letter.

Words are separated by spaces, possibly several in a row; keep every space
where it is. You may **not** use `.title()`, `.capitalize()` or `.split()`;
the tests check this. `.upper()` and `.lower()` on a single letter are fine.

## Task

- Create a function `to_title(text)` that returns the text with the first
  letter of every word in upper case and all other letters in lower case
- Create a function `count_words(text)` that returns the number of words
- Create a function `initials(text)` that returns the first letter of every
  word, in upper case, each followed by a dot

## Examples

| Call                                    | Returns              |
|-----------------------------------------|----------------------|
| `to_title("hello world")`               | `"Hello World"`      |
| `to_title("pYTHON")`                    | `"Python"`           |
| `to_title("  two  spaces ")`            | `"  Two  Spaces "`   |
| `count_words("  two  spaces ")`         | `2`                  |
| `count_words("   ")`                    | `0`                  |
| `initials("John Ronald Reuel Tolkien")` | `"J.R.R.T."`         |
| `initials("ada lovelace")`              | `"A.L."`             |

Hint: a letter starts a word when the character before it is a space — or
when there is nothing before it. Keep the previous character in a variable.
