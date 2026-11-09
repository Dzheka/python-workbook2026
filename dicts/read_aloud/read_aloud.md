# Read Aloud

Convert a number to its word equivalent.

## Task

Write a function `read_aloud(number)` that takes a string representation of a number (0-999) and returns the number spelled out in English words in uppercase.

- Return an empty string for empty input
- Input will only contain digit characters

## Template

```python
ONES = {
    0: 'ZERO', 1: 'ONE', 2: 'TWO', 3: 'THREE', 4: 'FOUR',
    5: 'FIVE', 6: 'SIX', 7: 'SEVEN', 8: 'EIGHT', 9: 'NINE'
}

TEENS = {
    10: 'TEN', 11: 'ELEVEN', 12: 'TWELVE', 13: 'THIRTEEN', 14: 'FOURTEEN',
    15: 'FIFTEEN', 16: 'SIXTEEN', 17: 'SEVENTEEN', 18: 'EIGHTEEN', 19: 'NINETEEN'
}

TENS = {
    20: 'TWENTY', 30: 'THIRTY', 40: 'FORTY', 50: 'FIFTY',
    60: 'SIXTY', 70: 'SEVENTY', 80: 'EIGHTY', 90: 'NINETY'
}


def read_aloud(number: str) -> str:
    pass


if __name__ == "__main__":
    print(read_aloud("7"))  # "SEVEN"
    print(read_aloud("15"))  # "FIFTEEN"
    print(read_aloud("42"))  # "FORTY TWO"
    print(read_aloud("90"))  # "NINETY"
    print(read_aloud("100"))  # "ONE HUNDRED"
    print(read_aloud("105"))  # "ONE HUNDRED FIVE"
    print(read_aloud("333"))  # "THREE HUNDRED THIRTY THREE"
    print(read_aloud("0"))  # "ZERO"
    print(read_aloud(""))  # ""
```
