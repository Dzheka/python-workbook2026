def caesar_cipher(text, shift):
    low = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    i = 0
    for char in text:
        if char in low:
            a = low.index(char)
            shifted_idx = (a + shift) % 26
            result += low[shifted_idx]
        elif char in upper:
            a = upper.index(char)
            shifted_idx = (a + shift) % 26
            result += upper[shifted_idx]
        else:
            result += char
    return result