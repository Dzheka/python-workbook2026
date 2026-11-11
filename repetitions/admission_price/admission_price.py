a = 0
while True:
    age = input()
    if age == '':
        print(f"${a:.2f}")
        break
    age = int(age)

    if age <= 2:
        a+=0
    elif 3 <= age <= 12:
        a+=14
    elif age >= 65:
        a+=18
    else:
        a+= 23