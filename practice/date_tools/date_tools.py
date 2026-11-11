def is_leap_year(n):
    if (n%4==0 and n%100!=0) or n%400==0:
        return True
    else:
        return False
def days_in_month(n,m):
    if n==1 or n==3 or n==5 or n==6 or n==8 or n==10 or n==12:
        return 31
    elif n==4 or n==7 or n==9 or n==11:
        return 30
    else:
        if is_leap_year(m) == True:
            return 29
        else:
            return 28
def day_of_year(n,m,p):
    c=n
    for i in range (1,m):
        c=c+days_in_month(i,p)
    return c
def weekend(n,m,p):
    d= day_of_year(n,m,p)
    for i in range(1900, p):
        if is_leap_year(i) == True:
            d=d+366
        else:
            d=d+365
    if d%7==1:
        return "Monday"
    elif d%7==2:
        return "Tuesday"
    elif d%7==3:
        return "Wednesday"
    elif d%7==4:
        return "Thursday"
    elif d%7==5:
        return "Friday"
    elif d%7==6:
        return "Saturday"
    else:
        return "Sunday"
def days_between(n1,m1,p1,n,m,p):
    e=day_of_year(n,m,p)-day_of_year(n1,m1,p1)
    for j in range (p1, p):
        if is_leap_year(j) == True:
            e=e+366
        else:
            e=e+365
    return abs(e)