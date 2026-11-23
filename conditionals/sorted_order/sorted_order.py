first = int(input())
second = int(input())
third = int(input())

if first == second == third:
    print("equal")
elif first <= second <= third:
    print("ascending")
elif first >= second >= third:
    print("descending")
else:
    print("random")
