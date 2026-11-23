text = str(input())
result = ""

for word in text:
    result = word + result


if result == text:
    print(f"`{text}` is a palindrome")
else:
    print(f"`{text}` is not a palindrome")
