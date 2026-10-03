text = input()
ispalindrome = True
n = len(text)
for i in range(n // 2):
    if text[i] != text[-(i + 1)]:
        ispalindrome = False
        break
if ispalindrome:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a polidrome")

