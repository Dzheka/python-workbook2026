first = float(input())
second = float(input())
third = float(input())

if first <= 0 or second <= 0 or third <= 0 or first + second + third != 180:
    print("Invalid Triangle")
elif first == 90 or second == 90 or third == 90:
    print("Right Triangle")
elif first > 90 or second > 90 or third > 90:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")
