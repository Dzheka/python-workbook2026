n = int(input())

for i in range(1, n + 1):
    for z in range (0,n-i):
        print(" ",end="")
    for z in range (0,(2*i)-1):
        print("*", end="")
    print()