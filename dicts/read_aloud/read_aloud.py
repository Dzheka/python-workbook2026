from unittest import result

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
    if not number:
        return ""

    n = int(number)
    if n == 0:
        return ONES[0]

    parts = []

    if n >= 100:
        hundreds = n // 100
        parts.append(f"{ONES[hundreds]} HUNDRED")
        n %= 100

    if n >= 20:
        tens = (n // 10) * 10
        parts.append(TENS[tens])
        n %= 10

    if 10 <= n <= 19:
        parts.append(TEENS[n])
    elif 1 <= n <= 9:
        parts.append(ONES[n])

    return " ".join(parts)

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