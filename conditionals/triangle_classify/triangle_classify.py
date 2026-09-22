a = int(input())
b = int(input())
c = int(input())
if a==b==c:
    print("equilateral")
elif a==b!=c or a!=b==c or a==c!=b:
    print("isosceles")
else :
    print("scalene")