a=float(input())
b=float(input())
c=int(input())
for i in range (1,c+1):
    if a*(b**(i-1))//1==a*(b**(i-1)):
        print(f"{a*(b**(i-1)):.0f}")
    else:
        print (f"{a*(b**(i-1))}")