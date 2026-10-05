a = input()
c = a.replace(" ", "")
palindrome = True
for i in range(len(c) // 2):
    if c[i] != c[-(i + 1)]:
        palindrome = False
if palindrome:
    print(f"`{a}` is a palindrome")
else:
    print(f"`{a}` is not a palindrome")