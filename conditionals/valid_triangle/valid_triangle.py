first = float(input())
second = float(input())
third = float(input())

if first > 0 and second > 0 and third > 0 and first + second > third and first + third > second and second + third > first:
    print("valid triangle")
else:
    print("invalid triangle")
