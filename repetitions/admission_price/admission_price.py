s = 0
while True:
    age = input()
    if age == '':
        print(f"${s:.2f}")
        break
    age = int(age)

    if age <= 2:
        s+=0
    elif 3 <= age <= 12:
        s+=14
    elif age >= 65:
        s+=18
    else:
        s+= 23
