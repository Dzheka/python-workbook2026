def below_100(n):
    if not (0 <= n <= 99):
        return "not in the range"
    numbers_20 = [
        'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen',
        'seventeen', 'eighteen', 'nineteen', 'twenty']
    numbers_dec = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    if n <= 20:
        return numbers_20[n]

    tens = n // 10
    ones = n % 10
    if ones == 0:
        return numbers_dec[tens]

    return f"{numbers_dec[tens]}-{numbers_20[ones]}"

def below_1000(n):
    if not (0 <= n <= 999):
        return "not in the range"
    if n < 100:
        return below_100(n)

    hundreds_digit = n // 100
    hundreds_word = f"{below_100(hundreds_digit)} hundred"
    remainder = n % 100

    if remainder == 0:
        return hundreds_word

    return f"{hundreds_word} {below_100(remainder)}"

def number_to_words(n):
    if not (n <= 999_999_999):
        return "not in the range"

    if n == 0:
        return "zero"

    parts = []

    if n < 0:
        parts.append('minus')
        n = abs(n)

    millions = n // 1_000_000
    thousands = (n % 1_000_000) // 1_000
    units = n % 1_000
    if millions > 0:
        parts.append(f"{below_1000(millions)} millions")

    if thousands > 0:
        parts.append(f"{below_1000(thousands)} thousands")

    if units > 0:
        parts.append(below_1000(units))

    return " ".join(parts)

"""
n  = int(input())
print(number_to_words(n))
"""

for i in range(0, -101, -1):
    print(number_to_words(i))