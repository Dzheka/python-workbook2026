def gregorian_to_ordinal(year, month , day):
    x=0
    ans=0
    if (year%4==0 and year%100!=0 ) or (year%4000==0) :
        m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        x=1
    else :
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
    for i in range(0,month-1):

        ans+=m[i]
    
    return ans+day
    