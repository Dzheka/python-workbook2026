"""For sides a, b, and c to form a valid triangle:

a + b > c
a + c > b
b + c > a
All three conditions must be true.

"""
a = int(input())
b = int(input())
c = int(input())

if (a + b > c) and (a + c > b) and (b + c > a):
    print('valid triangle')
else:
    print('invalid triangle')

