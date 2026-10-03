n = int(input())
m = int(input())
d = min(n, m)
while n % d != 0 or m % d != 0:
    d -= 1
print("The GCD is", d)