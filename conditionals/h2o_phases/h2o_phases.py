a = int(input())
if 0<a<100:
    print("liquid")
elif 100<a:
    print("gas")
elif a<0:
    print("solid")
elif a == 0:
    print("solid or liquid")
elif a == 100:
    print("liquid or gas")