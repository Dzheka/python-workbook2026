tot = 0
while True:
    a = input()
    if  a == "":
        break
    a = int(a)
    if a<=2:
        tot+=0
    elif a>=3 and a<=12:
        tot+=14
    elif a>=65:
        tot+=18
    else:
        tot+=23
print(f"${tot:.02f}")
