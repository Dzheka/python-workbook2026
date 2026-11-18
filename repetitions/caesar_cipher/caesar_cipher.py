# chr(ord('a') + i)

message = input()
n = int(input())
result = ''
for i in message:
    if 'a' <= i <= 'z':
        # Normalize 'a' to 0
        # add shift and wrap around using % 26
        # add back 'a' ASCII offset
        a = chr((ord(i) - ord('a') + n) % 26 + ord('a'))
        result += a
    elif 'A' <= i <= 'Z':
        a = chr((ord(i) - ord('A') + n) % 26 + ord('A'))
        result += a
    elif i == ' ':
        result += ' '

print(result)