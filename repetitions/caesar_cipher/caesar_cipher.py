message = input()
shift = int(input())
result = ""
for ch in message:
    if ch >= "A" and ch <= "Z":
        position = ord(ch) - ord("A")
        position = (position + shift) % 26
        result = result + chr(position + ord("A"))
    elif ch >= "a" and ch <= "z":
        position = ord(ch) - ord("a")
        position = (position + shift) % 26
        result = result + chr(position + ord("a"))
    else:
        result = result + ch
print(result)