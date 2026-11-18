def ordinal_to_gregorian(year, day_of_year):
    leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    days_in_month = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = 1

    for days in days_in_month:
        if day_of_year <= days:
            return (year, month, day_of_year)
        day_of_year -= days
        month += 1             
    