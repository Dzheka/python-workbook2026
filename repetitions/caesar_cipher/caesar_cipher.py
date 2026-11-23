a = input()
ender = int(input())
result = ""
for char in a:
    if char.isalpha():
        start = ord('A') if char.isupper() else ord('a')
        
        new_char = chr(start + (ord(char) - start + ender) % 26)
        result += new_char
    else:
        result += char

print(result)