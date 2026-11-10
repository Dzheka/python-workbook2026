a = float(input())
b = float(input())
c = float(input())

if a + b <= c or a + c <= b or b + c <= a:
    print("not a triangle")
elif a == b == c:
    print("equilateral")
elif a == b or a == c or b == c:
    print("isosceles")
else:
    print("scalene")