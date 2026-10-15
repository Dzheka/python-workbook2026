n = abs(float(input()))
m=0
if n==0:
    print(1)
else:
    while n>=1:
        n=n/10
        m=m+1
    print(m)
