def caesar_cipher(text, shift):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    i = 0
    for char in text:
        if char in abc:
            cur_inx = abc.index(char)
            shifted_idx = (cur_inx + shift) % 26
            result += abc[shifted_idx]
        elif char in abc_upper:
            cur_inx = abc_upper.index(char)
            shifted_idx = (cur_inx + shift) % 26
            result += abc_upper[shifted_idx]
        else:
            result += char
    return result