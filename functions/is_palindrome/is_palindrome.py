def is_palindrome(x):
    b=""
    c=""
    if len(x)>=4:
        for i in range (1, len(x)//2+1):
            b=b+x[i]
        d=x[::-1]
        for j in range (1, len(x)//2+1):
            c=c+d[j]
    elif len(x) == 3:
        b=x[0]
        c=x[2]
    elif len(x)==2:
        b=x[0]
        c=x[1]
    elif len(x)==1:
        b=""
        c=""
    else:
        b=""
        d=""
    if b==c:
        return True
    else:
        return False
print(is_palindrome("aab"))