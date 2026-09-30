total = 0
while True:
    a = input()
    if a == "":
        break
    age = int(a)
    if age <=2:
        total+=0
    elif 3<= age<=12:
        total+=14.00
    elif age>=65:
        total+=18.00
    else:
        total+=23.00
print(f"${total:.2f}")


