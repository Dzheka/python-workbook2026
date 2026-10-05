t=int(input())
if t < 0 :
    print("solid")
elif t==0 :
    print("solid or liquid")
elif t>0 and t<100 :
    print("liquid")
elif t==100 :
    print("liquid or gas")
else :
    print("gas")