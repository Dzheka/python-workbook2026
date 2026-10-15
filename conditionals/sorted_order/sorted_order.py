a = int(input())
b = int(input())
c = int(input())

if a == b and a == c and b == c:
    print("equal")
elif a <= b <= c:
    print("ascending")
elif a >= b >= c:
    print("descending")
else:
    print("random")
