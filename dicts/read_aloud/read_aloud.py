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

    if n < 10:
        return ONES[n]

    if n < 20:
        return TEENS[n]

    if n < 100:
        tens_part = (n // 10) * 10 
        ones_part = n % 10           
        if ones_part == 0:
            return TENS[tens_part]
        return f"{TENS[tens_part]} {ONES[ones_part]}"

    if n < 1000:
        hundreds_part = n // 100    
        remainder = n % 100          
        if remainder == 0:
            return f"{ONES[hundreds_part]} HUNDRED"
        return f"{ONES[hundreds_part]} HUNDRED {read_aloud(str(remainder))}"

    return ""