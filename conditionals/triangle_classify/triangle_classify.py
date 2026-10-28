first = float(input())
second = float(input())
third = float(input())

if first == second == third:
    print("equilateral")
elif first == second or first == third or second == third:
    print("isosceles")
else:
    print("scalene")
