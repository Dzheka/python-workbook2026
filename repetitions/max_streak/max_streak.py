n = input()
max = 0
a = 0
while n != "" :
    n = int(n)
    if n == 1 :
        a = a+1
    elif n == 0 :
        if a > max:
            max = a
            a = 0
        elif a <= max:
            max = max
    n = input()
if a > max:
    max = a
print(f"Maximum streak: {max}")