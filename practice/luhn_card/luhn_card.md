# Card Number Check (Hard)

Bank card numbers end with a check digit computed by the **Luhn algorithm**:

1. Starting from the rightmost digit, double every second digit
   (the 2nd, 4th, 6th, ... from the right)
2. If a doubled digit is greater than 9, subtract 9 from it
3. Add up all the digits

The number is valid if this sum is divisible by 10.

## Task

- Create a function `luhn_sum(number)` that returns the Luhn sum of a string
  of digits
- Create a function `is_valid_card(number)` that returns `True` if the string
  contains only digits, has at least 2 of them, and its Luhn sum is divisible
  by 10
- Create a function `check_digit(partial)` that returns the digit (0–9) that,
  added to the end of `partial`, makes a valid number
- Create a function `mask(number)` that replaces every character except the
  last four with `*`; a number of four characters or fewer is returned as is

## Examples

| Call                                | Returns              |
|-------------------------------------|----------------------|
| `luhn_sum("79927398713")`           | `70`                 |
| `luhn_sum("79927398710")`           | `67`                 |
| `is_valid_card("79927398713")`      | `True`               |
| `is_valid_card("4539148803436467")` | `True`               |
| `is_valid_card("4539148803436468")` | `False`              |
| `is_valid_card("12a4")`             | `False`              |
| `is_valid_card("0")`                | `False`              |
| `check_digit("7992739871")`         | `3`                  |
| `check_digit("453914880343646")`    | `7`                  |
| `mask("4539148803436467")`          | `"************6467"` |
| `mask("1234")`                      | `"1234"`             |
