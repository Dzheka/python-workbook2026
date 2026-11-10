year = int(input())
month = int(input())
day = int(input())

if month == 2:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        days_in_month = 29
    else:
        days_in_month = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    days_in_month = 30
else:
    days_in_month = 31

day = day + 1

if day > days_in_month:
    day = 1
    month = month + 1

if month > 12:
    month = 1
    year = year + 1

print(f"{year:04d}-{month:02d}-{day:02d}")