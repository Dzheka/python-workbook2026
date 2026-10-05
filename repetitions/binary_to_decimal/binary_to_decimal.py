a = input()
res = 0 
b = len(a)
for i in range (0,b):
    res = res*2
    res = res + int(a[i])
print(f"The decimal equivalent is {res}")