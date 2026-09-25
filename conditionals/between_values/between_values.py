"""Write a program that determines if a value b is between two other values a and c.

Examples
Example 1:

5
7
10
between"""

a = int(input())
b = int(input())
c = int(input())

if a <= b <= c or a >= b >= c:
    print('between')
else:
    print('not between')