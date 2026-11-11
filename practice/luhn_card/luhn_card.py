def luhn_sum(x):
    s=0
    for i in range (1,len(x),2):
        d=0
        if 2*int(x[i])>9:
            d=2*int(x[i])-9
        else:
            d=2*int(x[i])
        s=s+d
    print(s)
    for i in range (0,len(x),2):
        s=s+int(x[i])
    return s
print(luhn_sum("4539148803436467"))
def is_valid_card(x):
    h=0
    for i in range (1, len(x)):
        if x[i] in "1234567890":
            h=h
        else:
            h=h+1
    if h!=0 or luhn_sum(x)%10!=0 or len(x)<2:
        return False
    elif h==0 and len(x)>=2 and luhn_sum(x)%10==0:
        return True
print (is_valid_card("4539148803436467"))

    
        




    