def is_leap_year(a):
    if a%4 == 0 and (a%100 !=0 or a%400 == 0):
        return True
    else:
        return False
print (is_leap_year(2020))