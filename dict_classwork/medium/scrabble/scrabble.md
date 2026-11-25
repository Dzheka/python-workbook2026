# Scrabble (Medium)

In a word game every letter is worth some points:

| Points | Letters                       |
|--------|-------------------------------|
| 1      | a, e, i, o, u, l, n, s, t, r  |
| 2      | d, g                          |
| 3      | b, c, m, p                    |
| 4      | f, h, v, w, y                 |
| 5      | k                             |
| 8      | j, x                          |
| 10     | q, z                          |

A word scores the sum of its letters.

## Task

- Create a dictionary `SCORES` at the top of your file: letter → points
- Create a function `word_score(word)` that returns the score of `word`.
  Upper and lower case count the same; anything that is not a letter (a
  space, a dash, a digit) scores `0`
- Create a function `best_word(words)` that returns the word with the highest
  score. On a tie, the word that comes **first in the list** wins. An empty
  list gives `None`

## Examples

| Call                                     | Returns      |
|------------------------------------------|--------------|
| `word_score("cab")`                      | `7`          |
| `word_score("Quiz")`                     | `22`         |
| `word_score("")`                         | `0`          |
| `best_word(["cat", "dog", "zoo"])`       | `"zoo"`      |
| `best_word(["at", "ta"])`                | `"at"`       |

Hint: instead of typing 26 lines, loop over pairs like `("aeioulnstr", 1)`
and fill `SCORES` letter by letter. Then `SCORES.get(letter, 0)`.
