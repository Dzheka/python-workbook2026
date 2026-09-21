a = input()
d = a[0]
c = int(a[1])
if (d=="a" or d =="c" or d=="e" or d =="g") and c%2!=0:
    print("black")
elif (d=="b" or d =="d" or d=="f" or d =="h") and c%2==0:
    print("black")
else:
    print("white")