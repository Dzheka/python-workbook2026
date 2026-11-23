first = int(input())
middle = int(input())
last = int(input())

if first <= middle <= last or first >= middle >= last:
    print("between")
else:
    print("not between")
