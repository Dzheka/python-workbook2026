import math
def hex_decimal(hex_str):
    d = "0123456789ABCDEF"
    ans=0
    for i in range(0,len(hex_str)):
        ind=d.index(hex_str[i].upper())
        ans=ans*16+ind
    return ans