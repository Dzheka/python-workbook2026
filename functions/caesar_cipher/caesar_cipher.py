def caesar_cipher(text: str, shift: int) -> str:
    result = []
    
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - start + shift) % 26
            result.append(chr(start + shifted))
        else:
            result.append(char)
            
    return "".join(result)
