message = input()
shift = int(input())

result = ""

for char in message:
    if char.isalpha():
        base = ord("A") if char.isupper() else ord("a")
        pos = ord(char) - base
        new_pos = (pos + shift) % 26
        result += chr(new_pos + base)
    else:
        result += char

print(result)
