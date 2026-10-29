def s(n):
    b=set(n)
    a = sorted(b)
    if len(a) < 2:
        return None
    return a[-2]
print(s([4, 9, 2, 9, 7]))  

n = [4, 9, 2, 9, 7, 4]
r = []
for i in n:
    if i not in r:
        r.append(i)
print(r)      