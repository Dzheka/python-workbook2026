a=int(input())
if a == 0 :
    print("solid or liquid")
elif a == 100 :
    print("liquid or gas")
elif a < 0 :
    print("solid")
elif a > 0 and a < 100 :
    print("liquid")
else :
    print("gas")