# String Utilities for Conditionals

## String Operations for Conditional Logic

| Operation     | Example                                                                     | Purpose                                               |
|---------------|-----------------------------------------------------------------------------|-------------------------------------------------------|
| `==` operator | `"cat" == "dog"` # `False`<br>`"cat" == "cat"` # `True`                     | Compare strings for exact equality                    |
| `in` operator | `"a" in "hello"` # `False`<br>`"e" in "hello"` # `True`                     | Check if character/substring exists in string         |
| Unpacking     | `a, b = "hi"` # `a="h", b="i"`<br>`x, y, z = "cat"` # `x="c", y="a", z="t"` | Extract characters by unpacking string into variables |
| `len()`       | `len("hello")` # `5`                                                        | Get the number of characters in a string              |
| `ord()`       | `ord("A")` # `65`                                                           | Convert character to ASCII numeric value              |
| `chr()`       | `chr(65)` # `"A"`                                                           | Convert ASCII numeric value to character              |

## String Methods

| Method       | Example                                                                            | Purpose                                               |
|--------------|------------------------------------------------------------------------------------|-------------------------------------------------------|
| `.lower()`   | `"Hello".lower()` # `"hello"`                                                      | Convert to lowercase for case-insensitive comparisons |
| `.upper()`   | `"hello".upper()` # `"HELLO"`                                                      | Convert to uppercase                                  |
| `.title()`   | `"hello".title()` # `"Hello"`                                                      | Convert to title case (first letter capitalized)      |
| `.isdigit()` | `"5".isdigit()` # `True`<br>`"a".isdigit()` # `False`                              | Check if character is a digit (0-9)                   |
| `.isalpha()` | `"a".isalpha()` # `True`<br>`"5".isalpha()` # `False`                              | Check if character is a letter (a-z, A-Z)             |
| `.isalnum()` | `"a5".isalnum()` # `True`<br>`"a!".isalnum()` # `False`                            | Check if string contains only letters and digits      |
| `.isspace()` | `" ".isspace()` # `True`<br>`"\t".isspace()` # `True`<br>`"a".isspace()` # `False` | Check if character is whitespace (space, tab, etc.)   |
