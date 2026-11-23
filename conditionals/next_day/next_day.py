year = int(input())
month = int(input())
day = int(input())
leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
if month == 2:
    if leap:
        days_in_month = 29
    else:
        days_in_month = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    days_in_month = 30
else:
    days_in_month = 31
day += 1
if day > days_in_month:
    day = 1
    month += 1
if month > 12:
    month = 1
    year += 1
print(f"{year:04d}-{month:02d}-{day:02d}")