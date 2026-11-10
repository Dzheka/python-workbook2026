year = int(input())
month = int(input())
day = int(input())

if month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        max_days = 29
    else:
        max_days = 28
elif month == 4 or month == 6 or month == 9 or month == 11:
    max_days = 30
else:
    max_days = 31

day += 1

if day > max_days:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1

print(f"{year}-{month:02d}-{day:02d}")
