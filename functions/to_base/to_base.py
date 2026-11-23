def to_base(n,base):
    if n==0:
        return '0'
    d = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ans=""
    while n:
        ans+=d[n%base]
        n//=base

    return ans[::-1]
