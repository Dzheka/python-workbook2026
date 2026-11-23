def is_palindrome(s):
    polindrome = True
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    return True
print(is_palindrome("racecar"))