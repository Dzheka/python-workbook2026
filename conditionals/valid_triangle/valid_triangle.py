a = float(input())
b = float(input())
c = float(input())

if a + b > c and a + c > b and b + c > a:
    print("valid triangle")
else:
    print("invalid triangle")