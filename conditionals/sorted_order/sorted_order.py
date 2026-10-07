"""Equal: a == b == c (all three numbers are the same)
Ascending: a ≤ b ≤ c (and not all equal)
Descending: a ≥ b ≥ c (and not all equal)
Random: neither ascending, descending, nor equal"""

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print('equal')
elif a <= b <= c:
    print('ascending')
elif a >= b >= c:
    print('descending')
else:
    print('random')