# Text Messaging (T9)

Convert a message to old cellphone key presses.

## Task

Write a function `text_messaging(message)` that converts a text message to the sequence of key presses needed on an old
cellphone keypad (T9 style).

- Conversion is case-insensitive ('a' and 'A' are the same)
- Skip characters that have no keypad mapping

### T9 Keypad Layout

| Key | Symbols | Key | Symbols |
|-----|---------|-----|---------|
| 1   | .,?!:   | 6   | MNO     |
| 2   | ABC     | 7   | PQRS    |
| 3   | DEF     | 8   | TUV     |
| 4   | GHI     | 9   | WXYZ    |
| 5   | JKL     | 0   | space   |

## Template

```python
T9_KEYPAD = {
    'A': '2', 'B': '22', 'C': '222',
    'D': '3', 'E': '33', 'F': '333',
    'G': '4', 'H': '44', 'I': '444',
    'J': '5', 'K': '55', 'L': '555',
    'M': '6', 'N': '66', 'O': '666',
    'P': '7', 'Q': '77', 'R': '777', 'S': '7777',
    'T': '8', 'U': '88', 'V': '888',
    'W': '9', 'X': '99', 'Y': '999', 'Z': '9999',
    ' ': '0',
    '.': '1', ',': '11', '?': '111', '!': '1111', ':': '11111'
}


def text_messaging(message: str) -> str:
    pass


if __name__ == "__main__":
    print(text_messaging("HI"))  # "44444"
    print(text_messaging("HELLO"))  # "4433555555666"
    print(text_messaging("HI THERE"))  # "4444408443377733"
    print(text_messaging("HI!"))  # "444441111"
    print(text_messaging("A"))  # "2"
    print(text_messaging(""))  # ""
```
