c=""
def encode(x):
    d=1
    global c
    for i in range (1,len(x)):
        if x[i]==x[i-1]:
            d=d+1
        else:
            if d>=2:
                c=c+str(d)
            c=c+x[i-1]
        d=1
    if d>1:
        c=c+str(d)
    c=c+x[0]
    return c
b=""
def decode(n):
    global b
    for i in range (0,len(n)):
        if n[i] in "1234567890":
            for j in range (int(n[i])):
                b=b+n[i+1]
        elif n[i] not in "1234567890" and n[i-1] in "1234567890":
            continue
        else:
            b=b+n[i]
    return b
def is_worth_it(y):
    if len(encode(y)) < len(y):
        return True
    else:
        return False
print(encode("aaabccdd"))
print(encode("abc"))
print(encode("aabbaa"))
print(encode("aaaaaaaaaaaa"))
print(decode("3ab2c2d"))
print(decode("10x1y"))
print(is_worth_it("aaab"))
print(is_worth_it("aabb"))