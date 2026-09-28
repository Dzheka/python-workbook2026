s = input()


for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
        print(f"`{s}` is not a palindrome")
    else:
        print(f"`{s}` is a palindrome")
 