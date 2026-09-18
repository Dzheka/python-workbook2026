"""Logic
Check if any of the three pairs are equal:

a == b OR a == c OR b == c
Note
At least two must be equal (can be all three)
Handle all possible arrangements of equal pairs
Use logical OR to combine conditions"""

a = int(input())
b =int(input())
c = int(input())

if a == b:
    print('yes')
elif a == c:
    print('yes')
elif b == c:
    print('yes')
else:
    print('no')