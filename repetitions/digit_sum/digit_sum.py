import math 

c = int(input())
a = abs(c)
b = 0
while a > 0 :
    b+=(a%10)
    a=(a//10)
print (b)