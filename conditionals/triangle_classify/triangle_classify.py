a = float(input())
b = float(input())
c = float(input())

if a == b == c:
    print("equilateral")
elif a == b or b == c or a == c:
    print("isosceles")
else:
    print("scalene")
    