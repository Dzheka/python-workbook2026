n = int(input())
for i in range (0,n+1):
    for x in range (1,(n+1)-i):
        print(" ",end="")
    for j in range (1,i+1):
        print(j,end="")
    for z in range (i,1,-1):
        print(z-1,end="")
    print()