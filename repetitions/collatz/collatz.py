n = int(input())
for i in range (0,n):
    if n==1:
        print(1)
        break
    print(n,end=" ")
    while n != 1:
        if n%2==0:
            n=n//2
        elif n%2 != 0:
            n=n*3 + 1
        print(n,end=" ")