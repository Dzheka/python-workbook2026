a=float(input())
if a<0:
    print("solid")
elif 0<a<100:
    print("liquid")
elif a==100:
    print("liquid or gas")
elif a==0:
    print("solid or liquid")
else:
    print("gas")
