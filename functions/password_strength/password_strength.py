def password_strength(pwd):
    l=len(pwd)
    up=0
    low=0
    ch=0
    num=0
    sym="!@#$%^&*()_+-=[]{}|;:,.<>?"
    for i in range(l-1):
        if pwd[i].isupper():
            up=1
        if pwd[i].islower():
            low=1
        if pwd[i].isdigit():
            num=1
        for j in range(len(sym)-1):
            if pwd[i]==sym[j]:
                ch=1
                break
    cnt=up+low+ch+num
    if l>=12 and cnt>=3:
        return "strong"
    elif l>=8 and cnt>=2:
        return "medium"
    return "weak"
