a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("equal")
elif a <= b <= c:
    print("ascending")
elif a >= b >= c:
    print("descending")
else:
    print("random")