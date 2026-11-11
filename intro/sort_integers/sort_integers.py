a=float(input())
b=float(input())
c=float(input())
smallest=min(a,b,c)
largest=max(a,b,c)
middle=a+b+c-smallest-largest
print(f"{smallest:.0f}, {middle:.0f}, {largest:.0f}")
