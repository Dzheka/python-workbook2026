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


def morse_encode(text: str) -> str:
    result = ''
    for i in text.upper():
        item = MORSE_CODE.get(i)
        if item:
            result += item
            result += ' '
    return result.strip()

if __name__ == "__main__":
    print(morse_encode("SOS"))  # "... --- ..."
    print(morse_encode("HI THERE"))  # ".... .. / - .... . .-. ."
    print(morse_encode("123"))  # ".---- ..--- ...--"
    print(morse_encode("Hello"))  # ".... . .-.. .-.. ---"
    print(morse_encode(""))  # ""
    print(morse_encode("A"))  # ".-"