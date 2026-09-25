"""Write a program that determines whether a given year is a leap year.

Leap Year Rules
A year is a leap year if:

Divisible by 400 → Leap year
Divisible by 100 (but not 400) → Not leap year
Divisible by 4 (but not 100) → Leap year
All other years → Not leap year
Examples"""
year = int(input())
if year % 400 == 0:
    print('Leap year')
elif year % 100 == 0:
    print('Not leap year')
elif year % 4 == 0:
    print('Leap year')
else:
    print('Not leap year')