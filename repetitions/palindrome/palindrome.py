s = input()
flag = True
for i in range(1, len(s)):
    if s[i] == s[-(i+1)]:
        continue
    else:
        flag = False

if flag:
    print(f"`{s}` is a palindrome")
else:
    print(f"`{s}` is not a palindrome")