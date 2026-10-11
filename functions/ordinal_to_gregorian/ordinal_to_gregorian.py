def ordinal_to_gregorian(year, day_of_year):
    x=day_of_year
    month=1
    if (year%4==0 and year%100!=0 ) or (year%4000==0) :
        m = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else :
        m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    i=0
    while x-m[i]>0:
        month+=1
        x-=m[i]
        i+=1
    return (year , month , x)
    