a=float(input())
b=float(input())
c=float(input())
if a+b>c and b+c>a and a+c>b:
    print("valid triangle")
else:
    print("invalid triangle")