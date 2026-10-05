a = input()
b = len(a)
palindrome = 1
for i in range (0,b//2):
    if a[i] != a [-(i+1)]:
        palindrome = 0
        break
if palindrome == 1:
    print(f"'{a}' is a palindrome")
elif palindrome == 0:
    print(f"'{a}' is not a palindrome")
