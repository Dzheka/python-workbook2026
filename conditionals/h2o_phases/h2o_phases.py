temperature = float(input())

if temperature < 0:
    print("solid")
elif temperature == 0:
    print("solid or liquid")
elif temperature < 100:
    print("liquid")
elif temperature == 100:
    print("liquid or gas")
else:
    print("gas")
