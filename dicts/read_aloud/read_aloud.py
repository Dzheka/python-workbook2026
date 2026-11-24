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

def read_aloud(number):
    if number == "":
        return ""

    n = int(number)
    if n == 0:
        return "ZERO"

    words = []

    if n >= 100:
        words.append(ONES[n // 100] + " HUNDRED")
        n %= 100

    if 10 <= n <= 19:
        words.append(TEENS[n])
    else:
        if n >= 20:
            words.append(TENS[n // 10 * 10])
        if n % 10 != 0:
            words.append(ONES[n % 10])

    return " ".join(words)
