# Run-Length Encoding (Hard)

A simple way to shrink text with long runs of the same letter: write the
length of each run before the letter. A run of one letter is written without
a number.

```
"aaabccdd"  →  "3ab2c2d"
```

## Task

- Create a function `encode(text)` that compresses `text` (it contains only
  letters)
- Create a function `decode(code)` that turns a compressed string back into
  the original text; a count can have several digits: `"12a"` is twelve `a`
- Create a function `is_worth_it(text)` that returns `True` only if the
  encoded text is *shorter* than the original

For any text of letters, `decode(encode(text))` must give `text` back.

## Examples

| Call                     | Returns          |
|--------------------------|------------------|
| `encode("aaabccdd")`     | `"3ab2c2d"`      |
| `encode("abc")`          | `"abc"`          |
| `encode("aabbaa")`       | `"2a2b2a"`       |
| `encode("aaaaaaaaaaaa")` | `"12a"`          |
| `decode("3ab2c2d")`      | `"aaabccdd"`     |
| `decode("10x1y")`        | `"xxxxxxxxxxy"`  |
| `is_worth_it("aaab")`    | `True`           |
| `is_worth_it("aabb")`    | `False`          |

Hint for `decode`: collect digits into a string until you meet a letter; then
the collected digits are the count — or 1 if there were none.
