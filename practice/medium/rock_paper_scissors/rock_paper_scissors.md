# Rock, Paper, Scissors (Medium)

Moves are letters: `"R"` rock, `"P"` paper, `"S"` scissors. Rock beats
scissors, scissors beat paper, paper beats rock.

A match is two strings of the same length: the `i`-th letter of each is what
the two players showed in round `i`.

## Task

- Create a function `beats(a, b)` that returns `True` if move `a` beats
  move `b`
- Create a function `round_result(a, b)` that returns `1` if the first player
  wins the round, `2` if the second does, `0` for a draw
- Create a function `match_score(first, second)` that returns the score as
  `"wins of first:wins of second"`; draws count for nobody
- Create a function `match_winner(first, second)` that returns `"first"`,
  `"second"` or `"draw"`

## Examples

| Call                                  | Returns    |
|---------------------------------------|------------|
| `beats("R", "S")`                     | `True`     |
| `beats("S", "R")`                     | `False`    |
| `round_result("R", "P")`              | `2`        |
| `round_result("P", "P")`              | `0`        |
| `match_score("RPS", "SPR")`           | `"1:1"`    |
| `match_score("RRR", "PPP")`           | `"0:3"`    |
| `match_winner("RSP", "SPR")`          | `"first"`  |
| `match_winner("RPS", "SPR")`          | `"draw"`   |

Hint: `match_winner` is easier if it counts the wins itself rather than
taking the score string apart.
