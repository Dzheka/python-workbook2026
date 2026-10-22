def is_int(s):
    num=0
    sym=0
    for i in range(len(s)):
        if s[i]>='1' and s[i]<='9' or (s[i]=='0'):
            num+=1
        elif s[i]=='-' or s[i]=='+':
            sym+=1
        else :
            return False
    if sym>=1 and num<1:
        return False
    if sym>=1 and num>=1:
        return True
    if sym<1 and num<1:
        return False
    if sym<1 and num>=1:
        return True