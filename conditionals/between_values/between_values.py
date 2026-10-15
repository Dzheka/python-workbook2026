a = float(input())
b = float(input())
c = float(input())

if a <= b <= c:
    print("between")
elif c <= b <= a:
    print("between")    
else:
    print("not between")