message = input()
shift = int(input())
result = ""
for letter in message:
    if "a" <= letter <= "z":
        position = ord(letter) - ord("a")
        position = (position + shift) % 26
        result += chr(position + ord("a"))
    elif "A" <= letter <= "Z":
        position = ord(letter) - ord("A")
        position = (position + shift) % 26
        result += chr(position + ord("A"))
    else:
        result += letter
print(result)