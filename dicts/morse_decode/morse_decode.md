# Morse Code Decoder

Convert Morse code back to text.

## Task

Write a function `morse_decode(morse)` that converts Morse code back to readable text.

- Individual character codes are separated by single spaces
- Skip codes that have no character mapping

## Template

```python
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

MORSE_TO_CHAR = {v: k for k, v in MORSE_CODE.items()}


def morse_decode(morse: str) -> str:
    pass


if __name__ == "__main__":
    print(morse_decode("... --- ..."))  # "SOS"
    print(morse_decode(".... .. / - .... . .-. ."))  # "HI THERE"
    print(morse_decode(".---- ..--- ...--"))  # "123"
    print(morse_decode(""))  # ""
    print(morse_decode(".-"))  # "A"
    print(morse_decode(".... . .-.. .-.. ---"))  # "HELLO"
```
