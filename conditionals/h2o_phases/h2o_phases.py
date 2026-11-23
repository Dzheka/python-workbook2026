temperature = int(input())

if temperature < 0:
    print("solid")
elif temperature == 0:
    print("solid or liquid")
elif 0 < temperature < 100:
    print("liquid")
elif temperature == 100:
    print("liquid or gas")
elif temperature > 100:
    print("gas")