"""Write a program that determines if a 4-digit integer is a palindrome."""

n = input()

if n == n[::-1]:
    print('palindrome')
else:
    print('not palindrome')