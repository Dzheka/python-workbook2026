# Bulls and Cows (Hard)

One player thinks of a secret code, the other tries to guess it. The code is
4 digits, all different, and it does not start with `0`.

After each guess the guesser hears how close they are:

- a **bull** is a digit that is in the code *at the same position*
- a **cow** is a digit that is in the code *at a different position*

Secret `"1234"`, guess `"1243"`: `1` and `2` are bulls, `4` and `3` are cows.

## Task

- Create a function `is_valid_secret(code)` that returns `True` if `code` is
  4 digits, all different, not starting with `0`
- Create a function `bulls(secret, guess)` that returns the number of bulls
- Create a function `cows(secret, guess)` that returns the number of cows
- Create a function `score(secret, guess)` that returns:
  - `"invalid"` if the guess breaks the rules of a code
  - `"win"` if all four digits are bulls
  - otherwise a string like `"1B2C"` — bulls, then cows

Write `score` using the other three functions.

## Examples

| Call                          | Returns     |
|-------------------------------|-------------|
| `is_valid_secret("1234")`     | `True`      |
| `is_valid_secret("0123")`     | `False`     |
| `is_valid_secret("1123")`     | `False`     |
| `bulls("1234", "1243")`       | `2`         |
| `cows("1234", "1243")`        | `2`         |
| `score("1234", "1243")`       | `"2B2C"`    |
| `score("5823", "5381")`       | `"1B2C"`    |
| `score("1234", "5678")`       | `"0B0C"`    |
| `score("1234", "1234")`       | `"win"`     |
| `score("1234", "1123")`       | `"invalid"` |

Hint: to check that all digits differ, compare every pair — a loop inside a
loop.

## Bonus (not graded)

Under `if __name__ == "__main__":` write the game itself: a fixed secret, and
a `while` loop that reads guesses with `input()` and prints the score until
the player wins.
