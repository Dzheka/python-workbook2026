def decimal_hex(n):
    if n==0:
        return '0'
    d = "0123456789ABCDEF"
    res=""
    while n:
        res+=d[n%16]
        n//=16
    return res[::-1]
