import math 

a = abs(int(input()))
b = 0
if a==0:
    print(1)
else:
    while a>0:
        a=(a//10)
        b+=1
    print(b)