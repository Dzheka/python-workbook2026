import math 
a=int(input())
b=int(input())
c=int(input())
d=(b*b)-4*a*c
if d<0 :
    print("No real roots")

elif d==0 :
    x=abs(b/(2*a))
    print(f"1 root: {x:.2f}")
else :
    x1=(-b+math.sqrt(d))/(2*a)
    x2=(-b-math.sqrt(d))/(2*a)
    print(f"2 roots: {x2:.2f} and {x1:.2f}")
