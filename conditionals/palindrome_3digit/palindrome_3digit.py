"""
Write a program that determines if a 3-digit integer is a palindrome.

Examples
Example 1:

121
palindrome
Example 2:

123
not palindrome
"""

n = input()

if n == n[::-1]:
    print('palindrome')
else:
    print('not palindrome')