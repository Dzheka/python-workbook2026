# Flip a Dictionary (Super Easy)

A dictionary answers "what is the value for this key?". Sometimes you need
the opposite question: "which key has this value?".

## Task

- Create a function `invert(d)` that returns a **new** dictionary where every
  value becomes a key and every key becomes its value. You can assume all
  values are different
- Create a function `keys_for(d, value)` that returns all keys whose value is
  `value`, sorted. Here values **can** repeat

## Examples

| Call                                                     | Returns                     |
|----------------------------------------------------------|-----------------------------|
| `invert({"one": 1, "two": 2})`                           | `{1: "one", 2: "two"}`      |
| `invert({"red": "#f00", "blue": "#00f"})`                | `{"#f00": "red", "#00f": "blue"}` |
| `keys_for({"Ali": "A", "Bek": "B", "Sara": "A"}, "A")`   | `["Ali", "Sara"]`           |
| `keys_for({"Ali": "A"}, "C")`                            | `[]`                        |

Hint: a dict comprehension `{v: k for k, v in d.items()}`.
