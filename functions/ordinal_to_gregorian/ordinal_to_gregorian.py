def ordinal_to_gregorian(year, day_of_year):
    is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if is_leap:
        days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = 1
    day = day_of_year

    for month_length in days_in_months:
        if day <= month_length:
            break
        day -= month_length
        month += 1

    return (year, month, day)

print(ordinal_to_gregorian(2024, 1))