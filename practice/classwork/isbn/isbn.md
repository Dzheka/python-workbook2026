# ISBN Check (Hard)

Every book has an ISBN. The old format, **ISBN-10**, has 10 characters,
often split by hyphens or spaces: `0-306-40615-2`. The last character is a
check digit, and it may be `X`, which means 10.

An ISBN-10 is valid when you multiply the characters by 10, 9, 8, ..., 1 and
the sum is divisible by 11:

```
0·10 + 3·9 + 0·8 + 6·7 + 4·6 + 0·5 + 6·4 + 1·3 + 5·2 + 2·1 = 132 = 11 · 12
```

The new format, **ISBN-13**, is `978` + the first 9 digits of the ISBN-10 +
a new check digit. To find it, multiply the 12 digits by 1, 3, 1, 3, ...
in turn, add them up, and take the number that brings the sum up to the next
multiple of 10 (0 if it already is one).

## Task

- Create a function `clean(code)` that returns `code` without hyphens and
  spaces
- Create a function `is_valid_isbn10(code)` that returns `True` if, after
  cleaning, the code has 10 characters, the first nine are digits, the last is
  a digit or a capital `X`, and the checksum is divisible by 11
- Create a function `isbn13_check_digit(first12)` that takes a string of 12
  digits and returns the ISBN-13 check digit as an `int`
- Create a function `isbn10_to_13(code)` that returns the ISBN-13 as a string
  of 13 digits, or `"invalid"` if `code` is not a valid ISBN-10

## Examples

| Call                                  | Returns           |
|---------------------------------------|-------------------|
| `clean("0-306-40615-2")`              | `"0306406152"`    |
| `is_valid_isbn10("0-306-40615-2")`    | `True`            |
| `is_valid_isbn10("0-306-40615-3")`    | `False`           |
| `is_valid_isbn10("0-8044-2957-X")`    | `True`            |
| `is_valid_isbn10("X804429570")`       | `False`           |
| `isbn13_check_digit("978030640615")`  | `7`               |
| `isbn10_to_13("0-306-40615-2")`       | `"9780306406157"` |
| `isbn10_to_13("0-306-40615-3")`       | `"invalid"`       |
