a = float(input())
b = float(input())
c = float(input())
if a + b + c != 180 or a <= 0 or b <= 0 or c <= 0:
    print("Invalid Triangle")
elif a < 90 and b < 90 and c < 90:
    print("Acute Triangle")
elif a == 90 or b == 90 or c == 90:
    print("Right Triangle")
else:
    print("Obtuse Triangle")