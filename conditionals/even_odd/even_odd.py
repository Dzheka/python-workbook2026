"""Logic
If number % 2 == 0: even
If number % 2 != 0: odd
Note
Zero is considered even
The modulo operator % returns the remainder of division
Handle negative numbers (they follow the same rule)"""

number = int(input())

if number % 2 == 0:
    print("even")
else:
    print("odd")