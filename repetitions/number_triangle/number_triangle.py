n=int(input())
m=0
for i in range (1,n+1):
    for j in  range (1,i+1):
        m=m+j*(10**(i-j))
    print (m)
    m=0