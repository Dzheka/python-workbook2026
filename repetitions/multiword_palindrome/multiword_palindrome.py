text = input()
cleaned = text.replace(" ", "")
palindrome = True
for i in range(len(cleaned) // 2):
    if cleaned[i] != cleaned[-(i + 1)]:
        palindrome = False
        break
if palindrome:
    print(f"'{text}' is a palindrome")
else:
    print(f"'{text}' is not a palindrome")