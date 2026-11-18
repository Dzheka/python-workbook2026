def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def days_in_month(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29  
        else:
            return 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

def day_of_year(day, month, year):
    total = day
    for m in range(1, month):
        total += days_in_month(m, year)
    return total

def f(day, month, year):
    total = 0
    for y in range(1900, year):
        if is_leap_year(year):
            total += 366 
        else:
            total += 365
    return total + day_of_year(day, month, year) - 1

def weekday(day, month, year):
    names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    return names[f(day, month, year) % 7]

def days_between(day1, month1, year1, day2, month2, year2):
    first = f(day1, month1, year1)
    second = f(day2, month2, year2)
    return abs(second - first)