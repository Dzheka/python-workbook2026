a = input()
b = int(a)
c = int(a)
while a != "":
    a = int(a)
    if a>b:
        b=a
    else:
        b=b
    if c>a:
        c=a
    elif c<a:
        c=c
    a = input()
print(f"Minimum: {c}")
print(f"Maximum: {b}")