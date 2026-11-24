def gregorian_to_ordinal(year, month, day):
    leap = year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)
    days_in_month = [31, 29 if leap else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    day_of_year = day
    for i in range(month - 1):
        day_of_year += days_in_month[i]

    return day_of_year