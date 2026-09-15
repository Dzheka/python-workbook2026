a = int(input())
b = int(input())
c = int(input())

if a <= b <= c:
    print("between")
elif c <= b <= a:
    print("between")
else:
    print("not between")
