a = float(input())
b = float(input())
c = float(input())

if a + b + c != 180:
    print("Invalid Triangle")
elif a == 90 or b == 90 or c == 90:
    print("Right Triangle")
elif a > 90 or b > 90 or c > 90:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")