a=float(input())
b=float(input())
c=float(input())
if a<=b<c and not a==c:
    print("ascending")
elif c<=b<a and not a==c:
    print("descending")
elif not a==b==c:
    print("random")
else:
    print("equal")
    