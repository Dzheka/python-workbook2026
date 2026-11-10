# Roman Numeral to Integer

Convert a Roman numeral string to an integer.

## Task

Write a function `roman_to_int(roman)` that converts a Roman numeral string to its integer value.

- Roman numerals are written from largest to smallest, left to right, except for the subtraction cases: IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)
- Input will be a valid Roman numeral string

## Template

```python
ROMAN = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


def roman_to_int(roman: str) -> int:
    pass


if __name__ == "__main__":
    print(roman_to_int("III"))  # 3
    print(roman_to_int("IV"))  # 4
    print(roman_to_int("IX"))  # 9
    print(roman_to_int("LVIII"))  # 58
    print(roman_to_int("MCMXCIV"))  # 1994
    print(roman_to_int("I"))  # 1
    print(roman_to_int("XIV"))  # 14
```
