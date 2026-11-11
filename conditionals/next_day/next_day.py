year = int(input())
month = int(input())
day = int(input())

"""
check for the leap year
end of the year (month 12 and month 30 31 28 or 29) 
to determine which day is the last day of a month,
check the end day of the month
end of the month (30, 31 or 28 or 29)
just the next day
"""

leap_year = False
last_day_of_the_month = 31
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True

if str(month) in '469' or month == 11:
    last_day_of_the_month = 30
elif month == 2:
    if leap_year:
        last_day_of_the_month = 29
    else:
        last_day_of_the_month = 28
# else last day of the month is 31 as in the start


if month == 12 and day == 31:
    year += 1
    month = 1
    day = 1
elif day == last_day_of_the_month:
    month += 1
    day = 1
else:
    day+=1

print(f'{year}-{month:02d}-{day:02d}')