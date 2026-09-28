a = int(input())
if a<0:
    print("solid")
elif a == 0:
    print("solid or liquid")
elif a<100:
    print("liquid")
elif a == 100:
    print("liquid or gas")
else:
    print("gas")