a = int(input())
b = int(input())
c = int(input())

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    print("valid triangle")
else:
    print("invalid triangle")