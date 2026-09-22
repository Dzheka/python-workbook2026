p=input()
l=p[0]
n=int(p[1])
#print(n)
if (l=='a' or l=='c' or l=='e' or l=='g') and n%2!=0 :
    print("black")
elif (l=='b' or l=='d' or l=='f' or l=='h') and n%2==0 :
    print("black")
else :
    print("white")
