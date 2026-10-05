a = input() 
b = len(a)
cnt = 0
sym="!@#$%^&*()_+-=[]{}|;:,.<>?"
for i in range (0,b):
    if a[i]>="A" and a[i]<="Z":
        cnt+=1
        break
for x in range (0,b):
    if a[x]>="a" and a[x]<="z":
        cnt+=1
        break
for y in range (0,b):
    if a[y]>="0" and a[y]<="9":
        cnt+=1
        break
for z in range (0,b):
    if a[z] in sym:
        cnt+=1
        break
if b>=8:
    cnt+=1

if cnt==1:
    print("Very Weak")
elif cnt==2:
    print("Weak")
elif cnt==3:
    print("Medium")
elif cnt==4:
    print("Strong")
elif cnt==5:
    print("Very Strong")